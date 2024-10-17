import pandas as pd 
import numpy as np 

from config.extra_variable_column_info import succeed_actions_variables



class GetExtraFeatures: 

    """
    GetExtraFeatures Class

    This class provides methods to compute additional performance metrics for a given DataFrame 
    containing player or team statistics. The methods can generate new features related to 
    actions such as duels, fouls, passes, and shots, enhancing the original dataset for further 
    analysis or modeling.

    Key Features:
    - _create_extra_metrics: Generates a comprehensive set of new metrics by processing the 
    input DataFrame through various calculations.
    - _attatch_to_df: Repositions a new column next to a specified existing column in the DataFrame.
    - Metric calculations include:
    - Success rates of actions (succeed actions)
    - Differences between actual and expected values (x - expected x)
    - Eagerness in performing specific actions (e.g., runs, dribbles, shots)
    - Loose ball and offensive physical duels statistics
    - Calculation of foul-making metrics based on card averages
    - Shot quality assessments based on expected goals
    - Ratios of different types of passes to overall passing statistics
    
    The class requires a pandas DataFrame as input and outputs modified DataFrames with additional 
    metrics and new columns.
    """

    def __init__(self): 
        pass

    def _create_extra_metrics(self, new_df):
        """
        Create additional metrics based on the input DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame.
            succeed_metrics (bool): Whether to calculate successful actions.
            x_Ex (bool): Whether to calculate the difference between x and expected x.
            foul_calculation (bool): Whether to calculate foul metrics.
            eagerness_calculation (bool): Whether to calculate eagerness metrics.
            eagerness_column_setting (str or list): The setting for eagerness calculation columns.

        Returns:
            pd.DataFrame: The DataFrame with additional metrics added.
            list: The list of additional columns added.
        """

        new_df = self._loose_ball_duels_calc(new_df)
        new_df = self._offensive_phys_duels_calc(new_df)
        new_df = self._create_succeed_actions(new_df)
        new_df = self._x_minus_expected_x(new_df)
        new_df = self._foul_maker(new_df)
        new_df = self._eagerness_calculations(new_df)
        new_df = self._shot_quality_calculation(new_df)
        new_df = self._make_conceded_goals_bad(new_df)
        new_df = self._calculate_pass_ratios(new_df)

        return new_df


    def _attatch_to_df(self, df: pd.DataFrame, brother_column: str, new_column: str) -> pd.DataFrame:
        """
        Inserts a column from the DataFrame `df` next to a specified `brother_column` in the DataFrame.

        This function takes the input DataFrame `df`, and moves the specified `new_column` next to 
        the `brother_column` in the column order. The original DataFrame is modified by positioning 
        the `new_column` immediately after the `brother_column`. 

        Args:
            df (pd.DataFrame): The input DataFrame to which the new column will be repositioned.
            brother_column (str): The name of the column next to which the new column will be placed.
            new_column (str): The name of the column that needs to be repositioned.

        Returns:
            pd.DataFrame: The modified DataFrame with the new column placed next to the specified brother column.

        """
        index = df.columns.get_loc(brother_column)
        df = (
            df.iloc[:, : index + 1]
            .join(df.pop(new_column))
            .join(df.iloc[:, index + 1 :])
        )
        return df


    def _create_succeed_actions(self, df, succeed_actions_source=succeed_actions_variables):
        """
        Create new columns in a DataFrame based on specified numerical and percentage variables.

        Parameters:
        - df (pd.DataFrame): The input DataFrame.
        - succeed_actions_source (list): A list of tuples specifying pairs of numerical and percentage variables.

        Returns:
        - pd.DataFrame: A new DataFrame with additional columns calculated based on the specified source.

        Example:
        df = create_succeed_actions(input_df, succeed_actions_source=[('col1', 'col2'), ('col3', 'col4')])
        """

        # Create a copy of the input DataFrame to avoid modifying the original data
        new_df = df.copy()

        # Iterate over the specified numerical and percentage variable pairs
        for i in succeed_actions_source:
            numerical_variable = i[0]
            percentage_variable = i[1]

            # Calculate the new column based on the specified percentage and round the values
            new_df["succeed_" + numerical_variable] = np.round(
                new_df[numerical_variable] * (new_df[percentage_variable] / 100), 2
            )

            new_df = self._attatch_to_df(
                df=new_df,
                brother_column=numerical_variable,
                new_column="succeed_" + numerical_variable,
            )

        # Return the modified DataFrame with the new columns
        return new_df
    
    def _x_minus_expected_x(self, df):
        """
        Calculate the differences between certain columns and their expected values in a DataFrame.

        Parameters:
        - df (pd.DataFrame): The input DataFrame.

        Returns:
        - pd.DataFrame: A new DataFrame with additional columns representing the differences between certain columns and their expected values.

        Example:
        df_result = x_minus_expected_x(input_df)
        """

        # Calculate assists - expected assists
        df["xg_assists-assists"] = df["xg_assist_avg"] - df["assists_avg"]

        # Calculate goals - expected goals
        df["goals-xg_goals_avg"] = df["goals_avg"] - df["xg_shot_avg"]

        # Calculate non_pen_goals - expected non_pen_goals
        df["non_pen_goals-xg_goals_avg"] = df["non_penalty_goal_avg"] - (
            df["xg_shot_avg"] - ((df["goals_avg"] - df["non_penalty_goal_avg"]) * 0.76)
        )

        for i in [["xg_assist_avg", "xg_assists-assists"], ["goals_avg", "goals-xg_goals_avg"], ["non_penalty_goal_avg", "non_pen_goals-xg_goals_avg"]]:
            df = self._attatch_to_df(
                df= df,
                brother_column= i[0],
                new_column= i[1],
                )

        # Return the modified DataFrame with the new columns
        return df
    

    def _foul_maker(self, df):
        """
        Calculate the smart foul-making metric based on standardization of red cards, fouls, and yellow cards in a DataFrame.

        Parameters:
        - df (pd.DataFrame): The input DataFrame.

        Returns:
        - pd.DataFrame: A new DataFrame with an additional column representing the smart foul-making metric.

        Example:
        df_result = foul_maker(input_df)
        """

        # Define a function for standardization
        def standardize_func(x):
            mean_value = x.mean()
            std_value = x.std()
            return np.round((x - mean_value) / std_value, 2)

        # Calculate the smart foul-making metric based on standardization of red cards, fouls, and yellow cards
        df["foul_making_avg"] = (
            standardize_func(df["red_cards_avg"])
            + standardize_func(df["fouls_avg"])
            + standardize_func(df["yellow_cards_avg"])
        )

        # Multiply the calculated metric by -1
        df["foul_making_avg"] = df["foul_making_avg"] * -1

        # Find the index of the "red_cards_avg" column and reorder columns

        df = self._attatch_to_df(
            df= df,
            brother_column= "red_cards_avg",
            new_column= "foul_making_avg",
            )

        # Return the modified DataFrame with the new column
        return df
    

    def _eagerness_calculations(self, df):
            """
            Calculate eagerness metrics based on different types of actions.

            Args:
                df (pd.DataFrame): The DataFrame containing the data.

            Returns:
                pd.DataFrame: The DataFrame with eagerness metrics added.
            """

            # Define the columns that are needed to calculate the eagerness of those actions 
            run_columns = ["accelerations_avg", "progressive_run_avg"]
            dribble_columns = ["dribbles_avg"]
            forward_pass_columns = ["forward_passes_avg"]
            shot_columns = ["shots_avg"]
            cross_column = ["crosses_avg"]

            # Calculate the eagerness based on the variables defined above 
            df["run_eagerness"] = df[run_columns].sum(axis=1) / df["received_pass_avg"]
            df["dribble_eagerness"] = (df[dribble_columns].sum(axis=1) / df["received_pass_avg"])
            df["forward_pass_eagerness"] = (df[forward_pass_columns].sum(axis=1) / df["received_pass_avg"])
            df["shot_eagerness"] = df[shot_columns].sum(axis=1) / df["received_pass_avg"]
            df["cross_eagerness"] = (df[cross_column].sum(axis=1) / df["received_pass_avg"])


            for i in [[run_columns, "run_eagerness"], 
                      [dribble_columns, "dribble_eagerness"], 
                      [forward_pass_columns, "forward_pass_eagerness"], 
                      [shot_columns, "shot_eagerness"], 
                      [cross_column, "cross_eagerness"]
                      ]:

                df = self._attatch_to_df(
                    df = df,
                    brother_column= i[0][-1],
                    new_column= i[1],
                    )

            return df
    

    def _shot_quality_calculation(self, df):
        """
        Calculate shot quality by dividing expected goals (xg) per shot by the average number of shots in a DataFrame.

        Parameters:
        - df (pd.DataFrame): The input DataFrame.

        Returns:
        - pd.DataFrame: A new DataFrame with an additional column representing shot quality.

        """

        # Calculate shot quality by dividing xg per shot by the average number of shots
        df["shot_location_quality"] = df["xg_shot_avg"].fillna(0) / df[
            "shots_avg"
        ].fillna(0)

        df = self._attatch_to_df(
            df= df,
            brother_column= "xg_shot_avg",
            new_column= "shot_location_quality",
            )

        # Return the modified DataFrame with the new column
        return df
    

    def _calculate_pass_ratios(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate various pass ratios from average pass statistics.

        Parameters:
        - df (pd.DataFrame): DataFrame containing average pass statistics.

        Returns:
        - pd.DataFrame: The input DataFrame with additional columns for pass ratios.
        """
        
        # Calculate all progressive type ratios 
        df["forward_passes_ratio"] = df["forward_passes_avg"] / df["passes_avg"]
        df["key_passes_ratio"] = df["key_passes_avg"] / df["passes_avg"]
        df["through_passes_ratio"] = df["through_passes_avg"] / df["passes_avg"]
        df["passes_to_final_third_ratio"] = (df["passes_to_final_third_avg"] / df["passes_avg"])
        df["pass_to_penalty_area_ratio"] = (df["pass_to_penalty_area_avg"] / df["passes_avg"])

        return df
    

    def _loose_ball_duels_calc(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate loose ball duels statistics from duel averages.
        Note that this are indicative stats and not true values. 

        Parameters:
        - df (pd.DataFrame): DataFrame containing duel statistics.

        Returns:
        - pd.DataFrame: The input DataFrame with additional columns for loose ball duels.
        """
        
        # Calculate average loose ball duels
        df["loose_ball_duels_avg"] = (
            df["duels_avg"]
            - df["defensive_duels_avg"]
            - df["aerial_duels_avg"]
            - df["offensive_duels_avg"]
        )
        
        # Replace negative values with 0 for loose ball duels
        df["loose_ball_duels_avg"] = [
            0 if i < 0 else i for i in df["loose_ball_duels_avg"]
        ]

        # Create a temporary DataFrame for calculations
        temp_df = df.copy()
        
        # Calculate won duels based on the percentage of duels won
        temp_df["won_duels"] = df["duels_avg"] * (df["duels_won"] / 100)
        temp_df["won_air_duels"] = df["aerial_duels_avg"] * (
            df["aerial_duels_won"] / 100
        )
        temp_df["won_off_duels"] = df["defensive_duels_avg"] * (
            df["defensive_duels_won"] / 100
        )
        temp_df["won_def_duels"] = df["offensive_duels_avg"] * (
            df["offensive_duels_won"] / 100
        )

        # Calculate won loose ball duels
        temp_df["won_loose_duels"] = (
            temp_df["won_duels"]
            - temp_df["won_air_duels"]
            - temp_df["won_off_duels"]
            - temp_df["won_def_duels"]
        )
        
        # Replace negative values with 0 for won loose ball duels
        temp_df["won_loose_duels"] = [
            0 if i < 0 else i for i in temp_df["won_loose_duels"]
        ]

        # Calculate the percentage of loose ball duels won
        df["loose_ball_duels_won"] = (
            temp_df["won_loose_duels"] / temp_df["loose_ball_duels_avg"] * 100
        )
        
        # Clamp the values of loose ball duels won between 0 and 100
        df["loose_ball_duels_won"] = [
            0 if i < 0 else 100 if i > 100 else i for i in df["loose_ball_duels_won"]
        ]

        # Fill NaN values with 0 for loose ball duels average and won
        df["loose_ball_duels_avg"] = df["loose_ball_duels_avg"].fillna(0)
        df["loose_ball_duels_won"] = df["loose_ball_duels_won"].fillna(0)

        return df
    

    def _offensive_phys_duels_calc(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate offensive physical duels statistics from duel averages.

        Parameters:
        - df (pd.DataFrame): DataFrame containing offensive duel statistics.

        Returns:
        - pd.DataFrame: The input DataFrame with additional columns for offensive physical duels.
        """
        
        # Calculate average offensive physical duels
        df["offensive_physical_duels"] = df["offensive_duels_avg"] - df["dribbles_avg"]
        
        # Replace negative values with 0 for offensive physical duels
        df["offensive_physical_duels"] = [
            0 if i < 0 else i for i in df["offensive_physical_duels"]
        ]

        # Create a temporary DataFrame for calculations
        temp_df = df.copy()
        
        # Calculate won offensive duels based on the percentage of duels won
        temp_df["won_offensive_duels"] = df["offensive_duels_avg"] * (
            df["offensive_duels_won"] / 100
        )
        temp_df["won_dribbles"] = df["dribbles_avg"] * (
            df["successful_dribbles_percent"] / 100
        )

        # Calculate won offensive physical duels
        temp_df["won_offensive_physical_duels"] = (
            temp_df["won_offensive_duels"] - temp_df["won_dribbles"]
        )

        # Replace negative values with 0 for won offensive physical duels
        temp_df["won_offensive_physical_duels"] = [
            0 if i < 0 else i for i in temp_df["won_offensive_physical_duels"]
        ]

        # Calculate the percentage of offensive physical duels won
        df["offensive_physical_duels_won"] = (
            temp_df["won_offensive_physical_duels"]
            / temp_df["offensive_physical_duels"]
            * 100
        )
        
        # Clamp the values of offensive physical duels won between 0 and 100
        df["offensive_physical_duels_won"] = [
            0 if i < 0 else 100 if i > 100 else i
            for i in df["offensive_physical_duels_won"]
        ]

        # Fill NaN values with 0 for offensive physical duels and won
        df["offensive_physical_duels"] = df["offensive_physical_duels"].fillna(0)
        df["offensive_physical_duels_won"] = df["offensive_physical_duels_won"].fillna(0)

        return df
    
    def _make_conceded_goals_bad(self, df):
        """
        Negate the average number of conceded goals in a DataFrame.

        Parameters:
        - df (pd.DataFrame): The input DataFrame.

        Returns:
        - pd.DataFrame: A new DataFrame with the 'conceded_goals_avg' column negated.

        Example:
        df_result = make_conceded_goals_bad(input_df)
        """

        # Negate the average number of conceded goals
        df["conceded_goals_avg"] = np.negative(
            df["conceded_goals_avg"].where(df["conceded_goals_avg"].notna())
        )

        # Return the modified DataFrame with the negated 'conceded_goals_avg' column
        return df






