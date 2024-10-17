import requests
import pandas as pd
from bs4 import BeautifulSoup

"""
This class, `get_league_levels`, retrieves and processes competition ranking data from a specified URL. 

Key Functionality:
1. **retrieve_competition_ranking_data**:
    - Retrieves league ranking data for a specified range of years and quarters.
    - Extracts and cleans raw text data from the web, converting it into structured data.
    - Optionally stores the resulting data into a `.xlsx` file in Excel format for readabilility.
    - Allows customization of the range of ranking positions to fetch.

2. **_get_text_data**:
    - Sends a GET request to a dynamically constructed URL to retrieve raw HTML data based on year, quarter, and ranking range.

3. **_clean_web_text**:
    - Cleans and processes the raw text data by extracting ranking positions, league names, and scores.
    - Converts this cleaned data into a Pandas DataFrame for further processing.

Usage:
- This class can be used to extract historical league ranking data across multiple years and quarters.
- Data can either be returned as a Python dictionary or saved in compressed Parquet format for further analysis or reporting.
"""


class get_league_levels:
    def __init__(self):
        pass

    def retrieve_competition_ranking_data(
        self,
        start_year: int,
        end_year: int,
        store: bool = True,
        path: str = "storage/league_info/league_level_data.xlsx",
        min_pos: int = 1,
        max_pos: int = 500,
    ):
        
        """
    Retrieves competition ranking data for a specified range of years and stores 
    or returns the data in a concatenated DataFrame.

    Args:
        start_year (int): The starting year for the data retrieval (inclusive).
        end_year (int): The ending year for the data retrieval (exclusive).
        store (bool, optional): Whether to save the resulting data to an Excel file. 
            If True, the data is saved to the specified `path`. Defaults to True.
        path (str, optional): The file path where the Excel file will be saved 
            if `store` is True. Defaults to "storage/league_info/league_level_data.xlsx".
        min_pos (int, optional): The minimum ranking position to filter the data. 
            Defaults to 1.
        max_pos (int, optional): The maximum ranking position to filter the data. 
            Defaults to 500.

    Returns:
        pd.DataFrame or None: 
            - If `store` is False, returns a pandas DataFrame containing the competition 
              ranking data for all years and quarters in the specified range.
            - If `store` is True, returns None after saving the data to an Excel file.

    Functionality:
        - Iterates through the specified range of years and quarters (Q1 to Q4).
        - For each year and quarter, it retrieves the competition ranking data 
          using an internal method `_get_text_data`.
        - Cleans the data and converts it into a DataFrame using `_clean_web_text`.
        - Adds year and quarter columns to each DataFrame and stores them in a list.
        - Concatenates all DataFrames into a single DataFrame.
        - If `store` is True, saves the final DataFrame to the specified Excel file.
        - If `store` is False, returns the concatenated DataFrame.
        - Handles exceptions during data retrieval and file saving, printing appropriate 
          error messages if issues arise.
    
    Raises:
        Any exceptions encountered during data extraction or file saving will be 
        caught and logged, allowing the process to continue.
    """
        
    
        # make range of years:
        year_range = list(range(start_year, end_year, 1))

        # the quarters written the same as the URL link
        quarters = [1, 2, 3, 4]

        # Initialize an empty list to collect dataframes
        league_level_list = []

        for year in year_range:
            for quarter in quarters:
                try:
                    league_level_text = self._get_text_data(
                        year=year, quarter=quarter, min=min_pos, max=max_pos
                    )

                    if league_level_text == "":
                        print(
                            f"League levels of year: {year} quarter:Q{quarter} is empty"
                        )
                        pass
                    else:
                        # Clean the text and get the dataframe
                        league_level_df = self._clean_web_text(league_level_text)

                        # Add columns for year and quarter
                        league_level_df['year'] = year
                        league_level_df['quarter'] = f"Q{quarter}"

                        # Append the dataframe to the list
                        league_level_list.append(league_level_df)

                except Exception as e:
                    print(
                        f"Extracting the data and making it into a dataframe failed for year:{year} quarter:Q{quarter}. Error: {e}"
                    )

        # Concatenate all dataframes into one
        if league_level_list:
            combined_df = pd.concat(league_level_list, ignore_index=True)
        else:
            combined_df = pd.DataFrame()

        # Store the dataframe in an Excel file or return it
        if store:
            try:
                # Save the dataframe as an Excel file
                combined_df.to_excel(path, index=False)
                print(f"Data successfully saved to {path}")
            except Exception as e:
                print(f"Failed to save data to Excel. Error: {e}")
        else:
            return combined_df

    def _get_text_data(
        self,
        year: int,
        quarter: int,
        min: int = 1,
        max: int = 500,
    ):
        # Define the URL
        url = f"https://www.teamform.com/ranking_league_append.php?typeId=%25&domin=https%3A%2F%2Fwww.teamform.com%2F&dominLink=https%3A%2F%2Fwww.teamform.com%2Fen%2F&langDB=&year={year}&quarter={quarter}&isMobile=mobile&start={min}&end={max}"

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract the text from the webpage
            text = soup.get_text()
        else:
            print("Failed to retrieve webpage. Status code:", response.status_code)

        return text

    def _clean_web_text(self, text) -> pd.DataFrame:

        # Split the text into lines
        lines = [i for i in text.strip().split("\n") if i != ""]
        # Initialize lists to store data
        rankings = []
        scores = []
        leagues_name = []
        leagues_country = []

        # Process each line and extract data
        for i in range(0, len(lines), 3):
            rankings.append(int(lines[i]))
            scores.append(float(lines[i + 2]))

            # clean league because now its a combination of name and country 
            messy_league = lines[i + 1]
            leagues_country.append(messy_league.split("-")[0])
            leagues_name.append(messy_league.split("-")[1])


        # Create a pandas DataFrame
        df = pd.DataFrame({"rank": rankings, "leagues_name": leagues_name, "leagues_country" : leagues_country, "score": scores})

        return df

