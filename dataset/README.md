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

🔗 Access Prayas Energy Dataset:
https://dataverse.harvard.edu/dataverse/eMARC?q=&types=files&sort=dateSort&order=desc&page=1



