
import pandas as pd 
import numpy as np 

from config.pos_translation import pos_translation_dict
from config.wyscout_column_info import wyscout_personal_columns, wyscout_team_season_columns

class ComparePlayers:

    def __init__(self):
        pass

    def _calculate_statistical_comparisons(
        self,
        df: pd.DataFrame,
        pos_translation_list: dict = pos_translation_dict,
        standardize: bool = True,
        quantalize: bool = True,
    ):

        # Translate player positions based on the pos_translation_list
        df["main_position"] = (
            df["primary_position"].map(pos_translation_list).fillna("UNKNOWN")
        )

        # special columns is list containing all variables that are made inbetween but dont contain stats 
        special_columns = ["main_position", "possession_ratio", "no_possession_ratio"]

        to_compare_columns = [col for col in df.columns if col not in wyscout_personal_columns and col not in wyscout_team_season_columns and col not in special_columns]

        # Perform statistical comparisons for each specified column
        for i in to_compare_columns:
            print("start comparing players on the following criteria {}".format(i))
            df = self._recalculate_column(
                df,
                to_altered_column=i,
            )

        print("Finished comparing players")

        return df


    def _recalculate_column(
        self,
        df: pd.DataFrame,
        to_altered_column: str,
        compare_group_columns: list = ['division', 'league_country', 'league_competition', 'main_position'],
        fill_na: bool = False,  # New argument to allow conditional filling of NaNs
    ) -> pd.DataFrame:

        # Make a copy of the DataFrame to avoid modifying the original
        new_df = df.copy()

        # Optional: Fill missing values in the specified column with 0 if fill_na is True
        if fill_na:
            new_df[to_altered_column] = new_df[to_altered_column].fillna(0)

        # Group the DataFrame by specified columns
        grouped = new_df.groupby(compare_group_columns)

        # Calculate and update the columns for each group
        new_df[f"zscore_{to_altered_column}"] = grouped[to_altered_column].transform(
            lambda x: self._standardize_func(x)
        )

        new_df[f"quantile_{to_altered_column}"] = grouped[to_altered_column].transform(
            lambda x: self._quantile_func(x)
        )

        return new_df

    # Function to standardize a group
    def _standardize_func(self, x):
        if x.isnull().all():
            return x  # Return as is if all values are NaN
        mean_value = x.mean()
        std_value = x.std()
        return np.round((x - mean_value) / std_value, 2)

    # Function to calculate quantile ranks for a group
    def _quantile_func(self, x):
        if x.isnull().all():
            return x  # Return as is if all values are NaN
        quantile_rank = x.rank(pct=True)
        return np.round(quantile_rank, 2)
