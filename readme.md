# Wyscout Data Enrichment for Clubs

## Overview
This repository is a tool designed to help football clubs unlock more value from their existing Wyscout data. While many clubs already have access to Wyscout's resources, they often underutilize the data that is readily available to them. Although Wyscout data might not be as detailed as custom scouting platforms, it can still provide valuable insights, helping clubs identify potential signings based on Key Performance Indicators (KPIs) tailored to their playing style.

## Key Features
- **Configurable KPIs**: Clubs can customize the KPIs, their weights, and the measurement methods to suit their team's tactics and playing philosophy.
- **Position Mapping**: Modify position mapping in the `pos_translation` file to align with your club's positional framework.
- **Wyscout Column Handling**: If Wyscout adds extra columns or renames existing ones, adjustments can be made in the `wyscout_column_info` file.
- **Extra Variables**: Customize additional variables for action success calculations and position-adjusted (padj) statistics in the `extra_variable_column_info` file.
- **Scouting Reports**: Generate scouting reports with compressed KPIs, total scores, and z-scores based on the customized configurations.

## Setup Instructions

### 1. Place Wyscout Data
To get started, place your extracted or scraped data from Wyscout in the following folder:

```
storage/wyscout_data
```

Ensure that all necessary Wyscout data files are stored here for the pipeline to function correctly.

### 2. Install Dependencies
Before running the code, you need to install the required dependencies. You can do this by running:

```bash
pip install -r requirements.txt
```

Make sure you have all necessary Python packages installed for the scripts to run without issues.

### 3. Configurations
The settings for the KPIs and other parameters can be customized according to your club’s preferences.

- **KPI Methods**: In the `config/kpi_methods` folder, you can adjust the KPI definitions, their weights, and the formula for calculating the total score. This ensures the evaluation is in line with your tactical requirements.
- **Position Mapping**: You can update the position mapping logic in the `config/pos_translation` file if your club uses different positional terms.
- **Wyscout Column Info**: If Wyscout introduces new data columns or modifies existing ones, you can update these changes in the `config/wyscout_column_info`.
- **Extra Variable Column Info**: Adjustments for successful action calculations and position-adjusted (padj) metrics can be made in the `config/extra_variable_column_info`.

### 4. Running the ETL Pipeline
To initiate the ETL (Extract, Transform, Load) process for creating a database, use the `runner_db_creation.ipynb` Jupyter notebook. This notebook prepares and processes your Wyscout data for further analysis.

- **Test Parameter**: A `test` parameter is included for testing the pipeline before full execution. This can be useful to ensure everything is working as expected.

### 5. Generate Scouting Reports
Once the ETL process is complete, you can generate the final scouting report by running the `runner_scout_file_creation.ipynb` notebook. This will create an Excel file that includes:

- Compressed KPIs
- Total scores for each player
- Z-scores for all stats based on the settings in the config file

This file will help you quickly assess player performance and identify potential signings.

## Summary
This tool provides clubs with a customizable solution to maximize the value of their Wyscout data, allowing them to scout more effectively. By adjusting the configuration files, clubs can tailor the data output to fit their specific playing style, tactics, and scouting needs.

Feel free to explore and modify the repository to suit your club’s requirements. For any issues or further questions, please reach out.


## Disclaimer
Please note that the Wyscout scraper file is deliberately excluded from this repository and has been added to the `.gitignore` file. This decision is made to avoid any potential legal or ethical issues related to sharing a workaround for bypassing Wyscout's data export limitations (e.g., the 500-row export restriction). We strongly recommend that users ensure compliance with Wyscout's terms of service when using their platform and retrieving data.

Additionally, some files in the `storage` directory have been removed to prevent any accidental sharing or leakage of data that does not belong to me. This is to ensure the privacy and security of third-party data. Users of this repository should only populate the `storage` folder with data they have legally obtained and are authorized to use.

By using this repository, you agree to take responsibility for ensuring that your use of the data and tools complies with any applicable legal requirements.