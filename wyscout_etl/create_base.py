import pandas as pd
import numpy as np
import os
from config.wyscout_column_info import wyscout_pilot_columns, wyscout_score_columns, wyscout_team_season_columns, wyscout_personal_columns


class CreateWyscoutBase:
    """
    A class for creating and managing a base DataFrame from Wyscout player data.

    This class is designed to facilitate the processing of player season statistics 
    obtained from Wyscout by providing a structured way to load, clean, and organize 
    data into a single DataFrame. 

    Key functionalities include:
    - Retrieving CSV file names from a specified directory.
    - Combining multiple CSV files into one comprehensive DataFrame.
    - Cleaning up data by handling missing values and unnecessary columns.
    - Merging additional league information to enhance the dataset.
    - Providing a final DataFrame in a logical column order for further analysis.

    Attributes:
        None: The class does not maintain state between method calls.
    
    Methods:
        __init__(): Initializes the CreateWyscoutBase class.
        get_base(source_path): Processes CSV files to create the base DataFrame.
        _get_file_names(source_path): Retrieves a list of CSV filenames from the directory.
        _create_base_frame(file_names, base_path): Concatenates data from multiple CSV files into a single DataFrame.
        _get_melted_league_id_info(): Retrieves and transforms league ID information from an Excel file.
        clean_pilot_columns(df): Cleans pilot columns by replacing zeros with NaN.
        clean_wyscout_variables(df): Additional data cleaning for specific variables.
    """

    def __init__(self) -> None:
        """
        Initialize the CreateWyscoutBase class.
        """
        pass

    def get_base(self, source_path: str = r"storage\wyscout_data\player_season_stats") -> pd.DataFrame:
        """
        Create the base Wyscout dataframe by processing multiple CSV files and merging with league ID data.

        Args:
            source_path (str): The path to the directory containing Wyscout player season stats files.
                              Defaults to 'storage\\wyscout_data\\player_season_stats'.

        Returns:
            pd.DataFrame: The final cleaned and ordered dataframe containing Wyscout data.
        """
        # Get list of all files in the source directory
        file_names = self._get_file_names(source_path)

        # Create dataframe from all the paths
        full_df = self._create_base_frame(file_names, base_path=source_path)

        # Sometimes there are empty columns in the Wyscout data, resulting in unnamed columns
        if "Unnamed: 0" in full_df:
            full_df = full_df.drop("Unnamed: 0", axis=1)

        # Get the league_id info but in a melted format
        melted_df = self._get_melted_league_id_info()

        # Merge dataframes together
        full_df = full_df.merge(melted_df, how="inner", left_on=["league_id"], right_on=["league_id"])

        # Clean the pilot columns
        full_df = self.clean_pilot_columns(full_df)

        full_df = self.clean_wyscout_variables(full_df)

        # Create a logical column order
        full_df = full_df[wyscout_team_season_columns + wyscout_personal_columns + wyscout_score_columns]

        return full_df

    def _get_file_names(self, source_path: str) -> list[str]:
        """
        Retrieve all CSV filenames from the source directory.

        Args:
            source_path (str): The path to the directory containing files.

        Returns:
            list[str]: A list of CSV filenames in the directory.
        """
        # List all files in the source directory
        files = os.listdir(source_path)

        # Separate the files into a list of CSV filenames
        file_names_csv = [i for i in files if i.endswith(".csv")]

        return file_names_csv

    def _create_base_frame(self, file_names: list[str], base_path: str) -> pd.DataFrame:
        """
        Create a single DataFrame by concatenating data from multiple CSV files.

        Args:
            file_names (list[str]): A list of filenames to be processed.
            base_path (str): The directory where the files are located.

        Returns:
            pd.DataFrame: A concatenated DataFrame containing all the data from the CSV files.
        """
        # Create an empty DataFrame to store the final data
        full_df = pd.DataFrame()

        # Loop through each file in the source directory
        for filename in file_names:
            print(f"Importing: {filename}")
            temp_path = os.path.join(base_path, filename)
            df = pd.read_csv(temp_path)

            # Concatenate the current DataFrame with the full DataFrame
            full_df = pd.concat([full_df, df])

            print(f"Finished importing: {filename}\n")

        return full_df

    def _get_melted_league_id_info(self) -> pd.DataFrame:
        """
        Retrieve and transform league ID information by melting league ID columns for different years.

        Returns:
            pd.DataFrame: A melted DataFrame containing league information with columns for each year.
        """
        # Import DataFrame
        df = pd.read_excel(r"storage/league_id_main_competitions.xlsx")

        # Melt the DataFrame to unpivot the league_id columns
        df_melted = df.melt(
            id_vars=['league_country', 'league_competition', 'division', 'start_moment'],
            value_vars=[
                'league_id_2018', 'league_id_2019', 'league_id_2020',
                'league_id_2021', 'league_id_2022', 'league_id_2023', 'league_id_2024'
            ],
            var_name='year',
            value_name='league_id'
        )

        # Extract the year from the 'year' column (e.g., from 'league_id_2018' to just '2018')
        df_melted['year'] = df_melted['year'].str.extract(r'(\d{4})')

        # Drop rows where 'league_id' is NaN
        df_melted = df_melted.dropna(subset=['league_id'])

        return df_melted

    def clean_pilot_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean pilot columns by replacing zeros with NaN, indicating missing data instead of zero occurrences.

        Args:
            df (pd.DataFrame): The DataFrame containing Wyscout data.

        Returns:
            pd.DataFrame: The DataFrame with cleaned pilot columns.
        """
        # 0 entails that it isn't measured, not that the occurrence of the activity is 0
        df[wyscout_pilot_columns] = df[wyscout_pilot_columns].replace(0, np.nan)

        return df
    

    def clean_wyscout_variables(self, df):
        """ 
        place all other cleaning in this function
        """

        df["last_club_name"] = df["last_club_name"].fillna("National Team")

        return df

