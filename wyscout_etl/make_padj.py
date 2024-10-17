import pandas as pd
import numpy as np
from config.extra_variable_column_info import in_possession_variables, out_possession_variables

class PadjMaker:
    
    def __init__(self) -> None:
        """
        Initializes the PadjMaker class.
        """
        pass

    def _make_df_padj(
        self,
        df: pd.DataFrame,
        in_possession: list = in_possession_variables,
        out_possession: list = out_possession_variables
    ) -> pd.DataFrame:
        """
        Creates a possession-adjusted DataFrame by adjusting columns based on player possession
        and non-possession scenarios. The function computes new possession-adjusted columns for
        both in-possession and out-of-possession periods.

        Parameters:
        - df (pd.DataFrame): Input DataFrame containing game data.
        - in_possession (list): List of column names that should be adjusted based on player possession.
        - out_possession (list): List of column names that should be adjusted based on non-possession.

        Returns:
        - pd.DataFrame: A new DataFrame with additional possession-adjusted columns.
        """
        print('Testing if specific settings are correct:')
        
        # Ensure possession ratios are correctly calculated and available
        df = self._calculate_possession(df)

        # Adjust columns related to player possession (in-possession scenario)
        for column in in_possession:
            print(f"Adjusting possession for in-possession column: {column}")
            new_column_name = f'{column}_padj'
            
            # Calculate possession-adjusted value
            df[new_column_name] = df[column].div(df['possession_ratio'])
            df[new_column_name] = np.round(df[new_column_name], 2)

            # Insert the new possession-adjusted column next to the original column
            index = df.columns.get_loc(column)
            df = df.iloc[:, :index + 1].join(df.pop(new_column_name)).join(df.iloc[:, index + 1:])

        # Adjust columns related to non-possession (out-of-possession scenario)
        for column in out_possession:
            print(f"Adjusting possession for out-of-possession column: {column}")
            new_column_name = f'{column}_padj'
            
            # Calculate non-possession-adjusted value
            df[new_column_name] = df[column].div(df['no_possession_ratio'])
            df[new_column_name] = np.round(df[new_column_name], 2)

            # Insert the new possession-adjusted column next to the original column
            index = df.columns.get_loc(column)
            df = df.iloc[:, :index + 1].join(df.pop(new_column_name)).join(df.iloc[:, index + 1:])
        
        # Return the DataFrame with possession-adjusted columns
        return df

    def _calculate_possession(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculates the possession and non-possession ratios based on interceptions.
        These ratios will be used to adjust columns for possession and non-possession
        periods in the game.

        The possession ratio is capped between 0.3 and 0.7 to avoid extreme values.

        Parameters:
        - df (pd.DataFrame): Input DataFrame containing columns for possession-related calculations.

        Returns:
        - pd.DataFrame: The DataFrame with added 'possession_ratio' and 'no_possession_ratio' columns.
        """
        # Calculate possession and no possession ratios based on average interceptions
        df['possession_ratio'] = np.round(1 - (df['interceptions_avg'] * 1.5) / (df['possession_adjusted_interceptions'] * 2), 2).fillna(0.5)
        df['no_possession_ratio'] = np.round((df['interceptions_avg'] * 1.5) / (df['possession_adjusted_interceptions'] * 2), 2).fillna(0.5)

        # Safeguard: Ensure ratios stay within the range [0.3, 0.7]
        df['possession_ratio'] = [0.3 if i < 0.30 else (0.7 if i > 0.7 else i) for i in df['possession_ratio']]
        df['no_possession_ratio'] = [0.3 if i < 0.30 else (0.7 if i > 0.7 else i) for i in df['no_possession_ratio']]

        return df
