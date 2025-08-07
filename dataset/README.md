#Datasets

1.ComStock and ResStock Dataset-
The ComStock and ResStock datasets are both developed by the National Renewable Energy Laboratory (NREL) under the support of the U.S. Department of Energy (DOE) to model and analyze energy consumption in the built environment. These datasets use OpenStudio and EnergyPlus simulation engines, are calibrated using real-world data (like utility bills and smart meter readings), and are publicly accessible. Both provide high-resolution data, including annual and 15-minute time-series energy consumption, and are intended to support national efforts in energy efficiency, decarbonization, grid planning, and policy evaluation. They are released and maintained as part of the Open Energy Data Initiative (OEDI) and are regularly updated with expanded coverage, improved calibration, and new retrofit scenarios.

1.1. ComStock – Commercial Building Dataset
ComStock models the energy performance of the U.S. commercial building stock, including over 350,000 representative building models spanning more than 14 commercial building types like offices, schools, retail stores, warehouses, and hospitals. It incorporates data from the Commercial Building Energy Consumption Survey (CBECS) and other sources to reflect real-world building characteristics across various climate zones and geographies. The dataset provides both annual summaries and 15-minute end-use load profiles, offering detailed insights into energy use for HVAC, lighting, plug loads, refrigeration, and more. ComStock also supports dozens of retrofit scenarios—such as electrification, high-efficiency HVAC systems, lighting upgrades, and building envelope improvements—helping researchers, utilities, and policymakers evaluate energy-saving opportunities and demand-side management strategies. The results are accessible through the ComStock Data Viewer, as well as full downloadable datasets hosted on NREL's portals.

🔗 Access ComStock Dataset:
https://comstock.nrel.gov/page/datasets

1.2. ResStock – Residential Building Dataset
ResStock models the energy usage of the U.S. residential sector, including millions of simulated homes such as single-family, multifamily, and mobile homes. It leverages data from sources like the Residential Energy Consumption Survey (RECS) and the U.S. Census, and applies statistical sampling to represent diverse household characteristics—including building age, floor area, HVAC systems, insulation levels, appliance types, occupancy behavior, and income levels. ResStock provides annual energy consumption, carbon emissions, utility bills, energy burden, and 15-minute time-series data across major end-uses such as heating, cooling, water heating, lighting, and appliances. It features hundreds of upgrade packages covering energy efficiency, electrification, and retrofit combinations to assess impacts on energy use, emissions, and equity. ResStock is especially valuable for identifying high-burden households, evaluating retrofit policies, and advancing equitable decarbonization strategies in the housing sector.

🔗 Access ResStock Dataset:
https://resstock.nrel.gov/datasets


2. CER Dataset-
The CER (Commission for Energy Regulation) dataset contains real-world electricity consumption data collected from Irish households at approximately 30-minute intervals. It represents low-frequency smart meter readings that capture total household energy usage over time. Each household is associated with long, variable-length time series, often spanning thousands of time steps. Instead of detailed usage events, the dataset provides weak labels indicating only the presence or absence of specific appliances (e.g., washing machine, dishwasher, dryer) in each home, making it a challenging yet realistic setting for appliance detection. Due to the low sampling rate and lack of per-appliance monitoring, traditional NILM techniques are less effective, motivating the use of deep learning methods like Transformers. In the TransApp framework, the CER dataset is used alongside the Appliance Detection Framework (ADF) to divide long time series into fixed-length subsequences. These subsequences are then fed into a Transformer model that has been pretrained in a self-supervised manner and fine-tuned for appliance presence classification. The dataset plays a central role in evaluating how well the model can infer appliance ownership from aggregated household consumption. Overall, the CER dataset is valuable for advancing scalable, low-frequency appliance detection techniques using real smart meter data.

🔗 Access CER Dataset:
https://github.com/adrienpetralia/TransApp/tree/master/data


4. Prayas Energy Dataset-
The Prayas eMARC (Monitoring and Analysis of Residential Electricity Consumption) dataset is a rich, high-resolution smart metering dataset collected by Prayas (Energy Group) in India. It captures detailed electricity consumption data from 115 residential households across urban, semi-urban, and rural areas of Maharashtra and Uttar Pradesh, spanning from January 2018 to June 2020. Each household was equipped with two GPRS-enabled smart meters—one at the main supply line and another on a major appliance such as a refrigerator or air conditioner—recording minute-level data on active power, energy consumption, voltage, current, and power factor. This allows for both whole-house and appliance-level monitoring. The dataset also includes 15-minute aggregated versions of the same data, making it suitable for a variety of time-series modeling tasks. Alongside the consumption data, Prayas collected detailed household survey data, which includes appliance ownership, usage patterns, and socioeconomic details, enabling context-aware analysis. The sample was selected to ensure diversity across income levels and appliance types. The eMARC dataset supports research in areas such as load disaggregation, demand response, power quality assessment, energy behavior modeling, and the impact of socio-technical factors on electricity usage in Indian households. It is publicly available for academic and non-commercial research.

## Project Overview

The project implements a Non-Intrusive Load Monitoring (NILM) system that processes raw energy consumption data and uses machine learning models to identify specific appliances operating in households. The system works with data collected from smart meters at different time intervals (15-minute, 30-minute, and 1-hour) and applies various classification algorithms to detect appliance usage patterns.

## Repository Structure

```
AI IoT Lab/
├── 2019 Appliance Datasets/          # Appliance-specific datasets (2019 only)
│   ├── Air_Conditioners_dataset.csv
│   ├── Air_Coolers_dataset.csv
│   ├── Fridge_dataset.csv
│   ├── Heating_and_Cooling_appliances_dataset.csv
│   ├── Inverter_dataset.csv
│   ├── Kitchen_appliances_dataset.csv
│   ├── Lights_and_Fans_dataset.csv
│   ├── TV_dataset.csv
│   ├── Washing_Machine_dataset.csv
│   └── Water_heaters_dataset.csv
├── Overall Appliance Datasets/        # Complete appliance datasets (2018-2020)
│   ├── Air_Conditioners_dataset.csv
│   ├── Air_Coolers_dataset.csv
│   ├── Fridge_dataset.csv
│   ├── Heating_and_Cooling_appliances_dataset.csv
│   ├── Inverter_dataset.csv
│   ├── Kitchen_appliances_dataset.csv
│   ├── Lights_and_Fans_dataset.csv
│   ├── TV_dataset.csv
│   ├── Washing_Machine_dataset.csv
│   └── Water_heaters_dataset.csv
├── Codes/                             # Data processing and ML pipeline scripts
│   ├── 1HourDataProcessing.py
│   ├── 15MinuteDataProcessing.py
│   ├── 30MinuteDataProcessing.py
│   ├── AppliancePipeline.py
│   ├── NILMDataProcessor_2019.py
│   └── NILMDataProcessor.py
└── Prayas Datasets/                   # Raw and processed energy consumption data
    ├── 1_hour_data_enhanced.csv
    ├── 1_hour_data_with_household_id.csv
    ├── 15_minute_data_enhanced.csv
    ├── 15_minute_data_with_household_id.csv
    ├── 30_minute_data_enhanced.csv
    ├── 30_minute_data_with_household_id.csv
    ├── eMARC load blocks.csv
    ├── eMARC_household_survey_summary.xlsx
    └── Household-Deployment basic info.xlsx
```

## Data Processing Pipeline

### Phase 1: Time-Interval Data Processing

The raw energy consumption data is processed at three different time intervals:

1. **15-minute intervals** (`15MinuteDataProcessing.py`)
2. **30-minute intervals** (`30MinuteDataProcessing.py`)
3. **1-hour intervals** (`1HourDataProcessing.py`)

Each processing script converts the raw load blocks file and household deployment information into two dataset formats:

#### Basic Dataset Schema:
- `deployment_id`: Unique identifier for each deployment
- `block`: Time block identifier
- `date`: Date of measurement
- `Load (kW)`: Power consumption in kilowatts
- `household_id`: Unique household identifier

#### Enhanced Dataset Schema:
- `deployment_id`: Unique identifier for each deployment
- `block`: Time block identifier  
- `date`: Date of measurement
- `Load (kW)`: Power consumption in kilowatts
- `household_id_x`: Primary household identifier
- `household_id_y`: Secondary household identifier
- `Deployment type`: Type of smart meter deployment
- `Region`: Geographic region of the household
- `Household type`: Classification of household characteristics

### Phase 2: NILM Data Processing

Two specialized processors extract appliance-specific datasets:

- **`NILMDataProcessor.py`**: Processes complete dataset (January 1, 2018 - June 30, 2020)
- **`NILMDataProcessor_2019.py`**: Processes 2019-only dataset

**Data Quality Filtering**: Only households with at least 50% of the maximum number of readings as non-empty values are included in the final appliance datasets.

### Phase 3: Machine Learning Pipeline

The `AppliancePipeline.py` script implements a comprehensive machine learning pipeline with the following components:

#### Classification Tasks

**Single-Output Classification**: 
- Trains models on each of the 10 individual appliance datasets
- Predicts presence/absence of specific appliances

**Multi-Output Classification**:
- Groups appliances into 3 categories:
  - **Kitchen Appliances**: Mixer, Fridge, Microwave
  - **Lights and Fans**: Lights, Ceiling Fans
  - **Heating and Cooling**: Water Heater, Air Cooler, Air Conditioner

#### Machine Learning Models

The pipeline trains and evaluates 5 different algorithms:

1. **Random Forest**: Ensemble method using multiple decision trees
2. **XGBoost**: Gradient boosting framework optimized for performance
3. **Arsenal**: Time series classification ensemble method
4. **Rocket**: Random convolutional kernel transform for time series
5. **Lightning**: Fast linear models for large-scale machine learning

## Appliance Categories

### Individual Appliances (10 types):
- Air Conditioners
- Air Coolers  
- Refrigerators
- Water Heaters
- Inverters
- Televisions
- Washing Machines

### Appliance Groups (3 categories):
- Kitchen Appliances (combined)
- Lights and Fans (combined)
- Heating and Cooling (combined)

## Getting Started

### Prerequisites

```bash
# Required Python packages
pip install pandas numpy scikit-learn xgboost
pip install sktime  # for Arsenal and Rocket
pip install lightning-ml  # for Lightning models
```

### Running the Pipeline

1. **Data Processing**:
```bash
# Process data at different time intervals
python 15MinuteDataProcessing.py
python 30MinuteDataProcessing.py  
python 1HourDataProcessing.py
```

2. **NILM Dataset Generation**:
```bash
# Generate appliance-specific datasets
python NILMDataProcessor.py        # Full dataset (2018-2020)
python NILMDataProcessor_2019.py   # 2019 only
```

3. **Machine Learning Training**:
```bash
# Train and evaluate all models
python AppliancePipeline.py
```

## Data Sources

The project uses data from the eMARC (Energy Monitoring and Analytics for Rural Communities) initiative, which provides:

- **Load Blocks**: Raw energy consumption measurements
- **Household Survey**: Demographic and appliance ownership information  
- **Deployment Information**: Technical details about smart meter installations

## Results and Applications

This NILM system enables:

- **Energy Efficiency Analysis**: Identify high-consumption appliances
- **Demand Response**: Predict and manage peak energy usage
- **Appliance Monitoring**: Non-intrusive detection of appliance operations
- **Rural Energy Planning**: Understand consumption patterns in rural households
- **Smart Grid Integration**: Enable intelligent energy distribution systems

## Contributing

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest new features.

## License

This project is part of academic research. Please cite appropriately if using this work.

## Contact

For questions about this project, please refer to the AI IoT Lab documentation or contact the project maintainers.




