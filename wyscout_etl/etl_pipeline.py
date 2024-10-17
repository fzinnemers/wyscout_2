from wyscout_etl.create_base import CreateWyscoutBase
from wyscout_etl.create_extra_variables import GetExtraFeatures
from wyscout_etl.make_padj import PadjMaker
from wyscout_etl.make_comparison_stats import ComparePlayers
from wyscout_etl.calculate_totals import CalculateKPI
from datetime import datetime
import os

class ETLPipelines():

    def __init__(self): 
        pass 

    def create_general_db(self, test = False): 
        print("ETL Pipeline started...")

        # Start creating the base
        print("Step 1: Creating the base data")
        df = CreateWyscoutBase().get_base()

        if test: 
            df = df[0:500]
        
        # Adding extra features
        print("Step 2: Adding extra metrics")
        df = GetExtraFeatures()._create_extra_metrics(df)
        
        # Making the adjusted data
        print("Step 3: Adjusting the data by making stats possession adjusted")
        df = PadjMaker()._make_df_padj(df)
        
        # Calculating statistical comparisons between players
        print("Step 4: Calculating player comparisons")
        df = ComparePlayers()._calculate_statistical_comparisons(df)
        
        # Calculating KPIs and storing them
        print("Step 5: Calculating and storing KPIs")
        df = CalculateKPI().store_kpi_and_total(df, "general.py")
        
        # Generate a filename with the current datetime
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"wyscout_data_{current_time}.csv"
        file_path = os.path.join("storage", "db", file_name)
        
        # Saving the data to CSV
        print(f"Step 6: Saving data to {file_path}")
        df.to_csv(file_path, index=False)

        print("ETL Pipeline finished successfully.")
