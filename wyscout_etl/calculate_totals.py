import pandas as pd 
import numpy as np 
import importlib.util
import os

from config.pos_translation import pos_translation_dict


class CalculateKPI():

    def __init__(self) -> None:
        pass 

    def store_kpi_and_total(self, 
                            df, 
                            kpi_method, 
                            standardize = True,
                            quantilize = True
                            ):


        importance_values, kpi_scoring_values, total_score_values = self._import_variables_from_script(kpi_method)

        df = self._calculate_kpi_scores(df, kpi_scoring_values, standardize, quantilize)

        df = self._weighted_totals_calculation(df, total_score_values, importance_values)


        return df

    def _import_variables_from_script(self, kpi_method):
        script_base_path = "config\kpi_methods\\" 

        script_path = script_base_path + kpi_method

        # Get the absolute path of the script
        script_path = os.path.abspath(script_path)
        
        # Extract the module name from the script path
        module_name = os.path.splitext(os.path.basename(script_path))[0]
        
        # Create a module spec based on the script path
        spec = importlib.util.spec_from_file_location(module_name, script_path)
        
        # Create a new module based on the spec
        module = importlib.util.module_from_spec(spec)
        
        # Execute the module
        spec.loader.exec_module(module)
        
        # Get all variables defined in the module
        variables = {key: value for key, value in module.__dict__.items() if not key.startswith('__')}
        
        variables =  list(variables.values())

        importance_values = variables[0]
        kpi_scoring_values = variables[1]
        total_score_values = variables[2]

        return importance_values, kpi_scoring_values, total_score_values
            

        
    def _calculate_kpi_scores(self, df, score_dict, standardize, quantile):
        """
        Calculates KPI scores based on z-scores and quantiles, with options to standardize and adjust quantiles.
        
        Parameters:
        df (pd.DataFrame): The input DataFrame containing KPI data.
        score_dict (dict): Dictionary containing the weights for each KPI in different subcategories.
        standardize (bool): Flag to indicate whether z-scores should be calculated.
        quantile (bool): Flag to indicate whether quantiles should be calculated.
        
        Returns:
        pd.DataFrame: DataFrame with added KPI score columns.
        list: List of added column names.
        """

        df_orig_columns = df.columns.tolist()

        def calculate_scores(metric, prefix, sub_cat, temp_score_dict):
            for column, weight in temp_score_dict.items():
                df[f'{prefix}_{sub_cat}'] += weight * df[f'{metric}_{column}'].fillna(df[f'{metric}_{column}'].min())
                df[f'{prefix}_{sub_cat}'] = np.round(df[f'{prefix}_{sub_cat}'], 2)

                adj_column = f'{column}_padj' if f'{column}_padj' in df.columns else column
                df[f'{prefix}_{sub_cat}_padj'] += weight * df[f'{metric}_{adj_column}'].fillna(df[f'{metric}_{adj_column}'].min())
                df[f'{prefix}_{sub_cat}_padj'] = np.round(df[f'{prefix}_{sub_cat}_padj'], 2)

        if standardize:
            for sub_cat, temp_score_dict in score_dict.items():
                df[f'avg_zscore_{sub_cat}'] = 0
                df[f'avg_zscore_{sub_cat}_padj'] = 0
                calculate_scores('zscore', 'avg_zscore', sub_cat, temp_score_dict)

        if quantile:
            for sub_cat, temp_score_dict in score_dict.items():
                df[f'avg_quantile_{sub_cat}'] = 0
                df[f'avg_quantile_{sub_cat}_padj'] = 0
                calculate_scores('quantile', 'avg_quantile', sub_cat, temp_score_dict)

        return df
    

    def _weighted_totals_calculation(self, df, scoring_dict, importance_values):

        def calculate_total_scores(row, columns, weight):
            """
            Calculate weighted scores for given columns in a row.
            """
            return weight * row[columns].sum()


        zscore_scores = []
        quantile_scores = []
        zscore_scores_padj = []
        quantile_scores_padj = []

        for index, row in df.iterrows():
            if pd.isna(row['primary_position']):
                zscore_scores.append(np.nan)
                quantile_scores.append(np.nan)
                zscore_scores_padj.append(np.nan)
                quantile_scores_padj.append(np.nan)
                continue

            input_position = row['primary_position']
            mapped_value = pos_translation_dict.get(input_position)

            total_zscore = 0
            total_quantile_score = 0
            total_zscore_padj = 0
            total_quantile_score_padj = 0
            total_weight = 0

            if mapped_value is not None:
                temp_scoring_dict = scoring_dict[mapped_value]

                for importance_level, columns in temp_scoring_dict.items():
                    zscore_columns = [f'avg_zscore_{col}' for col in columns]
                    quantile_columns = [f'avg_quantile_{col}' for col in columns]
                    zscore_columns_padj = [f'avg_zscore_{col}_padj' for col in columns]
                    quantile_columns_padj = [f'avg_quantile_{col}_padj' for col in columns]

                    weight = importance_values.get(importance_level, 0)


                    total_zscore += calculate_total_scores(row, zscore_columns, weight)
                    total_zscore_padj += calculate_total_scores(row, zscore_columns_padj, weight)

                    total_quantile_score += calculate_total_scores(row, quantile_columns, weight)
                    total_quantile_score_padj += calculate_total_scores(row, quantile_columns_padj, weight)

                    total_weight += weight * len(columns)

            zscore_scores.append(np.round((total_zscore / total_weight if total_weight else np.nan), 2))
            quantile_scores.append(np.round((total_quantile_score / total_weight if total_weight else np.nan), 2))
            zscore_scores_padj.append(np.round((total_zscore_padj / total_weight if total_weight else np.nan), 2))
            quantile_scores_padj.append(np.round((total_quantile_score_padj / total_weight if total_weight else np.nan), 2))

        df['weighted_zscore_total'] = zscore_scores
        df['weighted_zscore_total_padj'] = zscore_scores_padj

        df['weighted_quantile_total'] = quantile_scores
        df['weighted_quantile_total_padj'] = quantile_scores_padj

        return df
