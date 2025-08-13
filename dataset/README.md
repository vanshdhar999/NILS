### List of Datasets Used in our experiments

| **Dataset** | **No. of Buildings** | **Interval (min)** | **No. of Loads** | **Load Names** |
|-------------|------------|--------------------|------------|----------------|
| [**Prayas**](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YJ5SP1)  | 118        | 15, 30, 60         | 7          | Inverter (65%), Air-coolers (30%), Air-conditioners (15%), Fridge (70%), TV (85%), Washing Machine (50%), Water Heater (40%) |
| [**Comstock**](https://comstock.nrel.gov/page/datasets)| 1000       | 15, 30, 60         | 6          | Cooling (76%), Fans (90%), Heat Rejection (11%), Heating (44%), Refrigeration (31%), Water Systems (72%) |
| [**Restock**](https://resstock.nrel.gov/datasets) | 1000       | 15, 30, 60         | 11         | Ceiling Fan (66%), Clothes Dryer (66%), Clothes Washer (68%), Cooling (75%), Fans (56%), Dishwasher (66%), Freezer (18%), Heating (26%), Heating Fans (72%), Hot Water (19%), Garage Lighting (28%) |
|[**CER**](https://github.com/adrienpetralia/TransApp/tree/master/data)    | 3482       | 30, 60             | 7          | Cooling (75%), Dishwasher (66%), Pluginheater (31%), Tumbledryer (68%), Washingmachine (98%), Waterheater (56%), Desktop Computer (47%) |

> **Note**: Percentages in parentheses indicate the proportion of buildings where the appliance is present.


###  ComStock – Commercial Building Dataset**

ComStock models the energy performance of the **U.S. commercial building stock**, covering over **350,000 representative building models** across **14+ commercial building types** such as offices, schools, retail stores, warehouses, and hospitals. It is based on data from the **Commercial Building Energy Consumption Survey (CBECS)** and other sources, ensuring realistic representation of building characteristics across various climate zones and geographies.

The dataset contains **15-minute resolution simulated load data** (generated using EnergyPlus models) for a large number of commercial buildings across the USA.  
For our work, we **randomly selected 1,000 commercial buildings** located in California. After data cleaning and filtering based on load characteristics, we obtained appliance-level time-series load profiles for the following **six major appliance categories**:  

- Cooling (**760** samples)  
- Fans (**900** samples)  
- Heat Rejection (**110** samples)  
- Heating (**440** samples)  
- Refrigeration (**310** samples)  
- Water Systems (**720** samples)  

> The numbers in parentheses indicate the actual number of available samples for each appliance category.

The original dataset is recorded at **15-minute intervals** from **January 1, 2018** to **January 1, 2019**.  
For our experiments, we also converted the data to **30-minute** and **60-minute** intervals to match other datasets and test model robustness at different temporal resolutions.

**⚠ Note:**  
In this repository, **only one week of ComStock data** is included due to space constraints.  

🔗 **Download the full dataset:** [ComStock Data Portal](https://comstock.nrel.gov/)

![ComStock Appliance Count](https://quickchart.io/chart?width=700&height=400&c=%7B%22type%22%3A%22bar%22%2C%22data%22%3A%7B%22labels%22%3A%5B%22Cooling%22%2C%22Fans%22%2C%22Heat%20Rejection%22%2C%22Heating%22%2C%22Refrigeration%22%2C%22Water%20Systems%22%5D%2C%22datasets%22%3A%5B%7B%22label%22%3A%22Number%20of%20Samples%22%2C%22data%22%3A%5B760%2C900%2C110%2C440%2C310%2C720%5D%2C%22backgroundColor%22%3A%5B%22%234e79a7%22%2C%22%23f28e2b%22%2C%22%23e15759%22%2C%22%2376b7b2%22%2C%22%2359a14f%22%2C%22%23edc949%22%5D%7D%5D%7D%2C%22options%22%3A%7B%22indexAxis%22%3A%22y%22%2C%22scales%22%3A%7B%22x%22%3A%7B%22beginAtZero%22%3Atrue%7D%7D%2C%22plugins%22%3A%7B%22legend%22%3A%7B%22display%22%3Afalse%7D%2C%22title%22%3A%7B%22display%22%3Atrue%2C%22text%22%3A%22ComStock%20Appliance%20Sample%20Counts%22%7D%7D%7D%7D)



### **2. ResStock – Residential Building Dataset**

ResStock models the **energy usage of the U.S. residential sector**, simulating millions of homes across categories such as **single-family**, **multifamily**, and **mobile homes**.  
It leverages data from sources like the **Residential Energy Consumption Survey (RECS)** and the **U.S. Census**, and applies statistical sampling to represent diverse household characteristics, including:

- Building age and floor area  
- HVAC system types and insulation levels  
- Appliance ownership and usage  
- Occupancy patterns and income levels  

ResStock provides **annual energy consumption**, **carbon emissions**, **utility bills**, **energy burden**, and **15-minute time-series data** across major end uses such as heating, cooling, water heating, lighting, and appliances.

For our work, we **randomly selected 1,000 residential buildings** located in California. After data cleaning and filtering based on load characteristics, the ResStock dataset contains **appliance-level energy consumption profiles** for the following **11 categories**:

- Ceiling Fan (**660** samples)  
- Clothes Dryer (**660** samples)  
- Clothes Washer (**680** samples)  
- Cooling (**750** samples)  
- Fans (**560** samples)  
- Dishwasher (**660** samples)  
- Freezer (**180** samples)  
- Heating (**260** samples)  
- Heating Fans (**720** samples)  
- Hot Water (**190** samples)  
- Garage Lighting (**280** samples)  

> The numbers in parentheses indicate the actual number of available samples for each appliance category.

The original dataset is recorded at **15-minute intervals** from **January 1, 2018** to **January 1, 2019**.  
Similar to the ComStock dataset, we also generated **30-minute** and **60-minute** versions to allow analysis at different temporal resolutions.

**⚠ Note:**  
Due to Space Constraints we haven't uploaded our dataset here.  

🔗 **Download the full dataset:** [ResStock Data Portal](https://resstock.nrel.gov/)

![Restock Appliance Count](https://quickchart.io/chart?width=700&height=500&c=%7B%22type%22%3A%22bar%22%2C%22data%22%3A%7B%22labels%22%3A%5B%22Ceiling%20Fan%22%2C%22Clothes%20Dryer%22%2C%22Clothes%20Washer%22%2C%22Cooling%22%2C%22Fans%22%2C%22Dishwasher%22%2C%22Freezer%22%2C%22Heating%22%2C%22Heating%20Fans%22%2C%22Hot%20Water%22%2C%22Garage%20Lighting%22%5D%2C%22datasets%22%3A%5B%7B%22label%22%3A%22Number%20of%20Samples%22%2C%22data%22%3A%5B660%2C660%2C680%2C750%2C560%2C660%2C180%2C260%2C720%2C190%2C280%5D%2C%22backgroundColor%22%3A%5B%22%234e79a7%22%2C%22%23f28e2b%22%2C%22%23e15759%22%2C%22%2376b7b2%22%2C%22%2359a14f%22%2C%22%23edc949%22%2C%22%23af7aa1%22%2C%22%2394a4a2%22%2C%22%23ff9da7%22%2C%22%238cb369%22%2C%22%23f4a259%22%5D%7D%5D%7D%2C%22options%22%3A%7B%22indexAxis%22%3A%22y%22%2C%22scales%22%3A%7B%22x%22%3A%7B%22beginAtZero%22%3Atrue%7D%7D%2C%22plugins%22%3A%7B%22legend%22%3A%7B%22display%22%3Afalse%7D%2C%22title%22%3A%7B%22display%22%3Atrue%2C%22text%22%3A%22Restock%20Appliance%20Sample%20Counts%22%7D%7D%7D%7D)


### **2. CER – Commission for Energy Regulation Dataset**

The CER dataset contains real-world electricity consumption data collected from **Irish households** at approximately **30-minute intervals**. It represents low-frequency smart meter readings that capture total household energy usage over extended periods. Each household is associated with long, variable-length time series, often spanning thousands of time steps.

Unlike high-frequency datasets, CER provides **weak labels** indicating only the presence or absence of specific appliances (e.g., washing machine, dishwasher, dryer) in each home, without detailed per-appliance monitoring. This low sampling rate and lack of event-level data make traditional NILM approaches less effective, motivating the use of deep learning methods such as Transformers.

In the **TransApp framework**, the CER dataset is used alongside the Appliance Detection Framework (ADF) to segment long time series into fixed-length subsequences, which are then fed into a pretrained Transformer model fine-tuned for appliance presence classification.

For our work, we use data from **3,462 buildings** (out of the original 4,225) at **30-minute** and **60-minute** intervals, covering the following **seven appliance categories**:  
- Cooling  
- Dishwasher  
- Plug-in Heater  
- Tumble Dryer  
- Washing Machine  
- Water Heater  
- Desktop Computer  

**⚠ Note:**  
We do not currently have complete access to the full CER dataset. Our professor has formally requested permission to obtain the complete data from the source. Once access is granted, we will proceed with further experiments and extended analysis.  

🔗 **Dataset link:** [CER Dataset (TransApp)](https://github.com/adrienpetralia/TransApp/tree/master/data)

![CER Appliance Count](https://quickchart.io/chart?width=700&height=400&c=%7B%22type%22%3A%22bar%22%2C%22data%22%3A%7B%22labels%22%3A%5B%22Cooling%22%2C%22Dishwasher%22%2C%22PluginHeater%22%2C%22TumbleDryer%22%2C%22Washing%20Machine%22%2C%22Water%20Heater%22%2C%22Desktop%20Computer%22%5D%2C%22datasets%22%3A%5B%7B%22label%22%3A%22Percentage%20of%20Buildings%22%2C%22data%22%3A%5B75%2C66%2C31%2C68%2C98%2C56%2C47%5D%2C%22backgroundColor%22%3A%5B%22%234e79a7%22%2C%22%23f28e2b%22%2C%22%23e15759%22%2C%22%2376b7b2%22%2C%22%2359a14f%22%2C%22%23edc949%22%2C%22%23af7aa1%22%5D%7D%5D%7D%2C%22options%22%3A%7B%22indexAxis%22%3A%22y%22%2C%22scales%22%3A%7B%22x%22%3A%7B%22beginAtZero%22%3Atrue%2C%22max%22%3A100%7D%7D%2C%22plugins%22%3A%7B%22legend%22%3A%7B%22display%22%3Afalse%7D%2C%22title%22%3A%7B%22display%22%3Atrue%2C%22text%22%3A%22CER%20Appliance%20Presence%20(Percentage%20of%20Buildings)%22%7D%7D%7D%7D)



### Prayas Energy Dataset-
### **3. Prayas Energy Dataset**

The **Prayas eMARC** (*Monitoring and Analysis of Residential Electricity Consumption*) dataset is a **high-resolution smart metering dataset** collected by **Prayas (Energy Group)** in India.  
It captures detailed electricity consumption data from **115 residential households** across **urban**, **semi-urban**, and **rural** areas of **Maharashtra** and **Uttar Pradesh**, covering the period **January 2018 to June 2020**.

Each household was equipped with **two GPRS-enabled smart meters**:  
- One installed at the **main supply line**  
- One installed on a **major appliance** (e.g., refrigerator, air conditioner)  

The dataset records **minute-level measurements** of:  
- Active power  
- Energy consumption  
- Voltage  
- Current  
- Power factor  

This enables both **whole-house** and **appliance-level monitoring**.  
Additionally, the dataset includes **15-minute aggregated versions**, making it suitable for a wide range of time-series analysis tasks.

Alongside energy measurements, Prayas also conducted a **household survey**, capturing:  
- Appliance ownership  
- Usage patterns  
- Socioeconomic details  

This contextual information allows for **behavior-aware analysis** of energy use patterns.

For our work, we utilize **data from 118 households**, aggregated into **three temporal resolutions**:  
- **15 minutes**  
- **30 minutes**  
- **60 minutes**  

We focus on **seven appliance categories**, with the percentage indicating the proportion of households owning each appliance:  
- Inverter (**65%**)  
- Air Cooler (**30%**)  
- Air Conditioner (**15%**)  
- Fridge (**70%**)  
- TV (**85%**)  
- Washing Machine (**50%**)  
- Water Heater (**40%**)  

**Research applications** of the Prayas eMARC dataset include:  
- Non-Intrusive Load Monitoring (NILM)  
- Demand response modeling  
- Power quality assessment  
- Energy behavior analysis  
- Studying the influence of socio-technical factors on consumption  

**⚠ Note:**  
Due to Space constraints we havent't uploaded this dataset here. 
The complete dataset is publicly available for academic and non-commercial research.

🔗 **More information:** [Prayas eMARC Dataset](https://energy.prayaspune.org/)

![Prayas Appliance Count](https://quickchart.io/chart?width=700&height=400&c=%7B%22type%22%3A%22bar%22%2C%22data%22%3A%7B%22labels%22%3A%5B%22Inverter%22%2C%22Air-Cooler%22%2C%22Air-Conditioner%22%2C%22Fridge%22%2C%22TV%22%2C%22Washing%20Machine%22%2C%22Water%20Heater%22%5D%2C%22datasets%22%3A%5B%7B%22label%22%3A%22Percentage%20of%20Buildings%22%2C%22data%22%3A%5B65%2C30%2C15%2C70%2C85%2C50%2C40%5D%2C%22backgroundColor%22%3A%5B%22%234e79a7%22%2C%22%23f28e2b%22%2C%22%23e15759%22%2C%22%2376b7b2%22%2C%22%2359a14f%22%2C%22%23edc949%22%2C%22%23af7aa1%22%5D%7D%5D%7D%2C%22options%22%3A%7B%22indexAxis%22%3A%22y%22%2C%22scales%22%3A%7B%22x%22%3A%7B%22beginAtZero%22%3Atrue%2C%22max%22%3A100%7D%7D%2C%22plugins%22%3A%7B%22legend%22%3A%7B%22display%22%3Afalse%7D%2C%22title%22%3A%7B%22display%22%3Atrue%2C%22text%22%3A%22Prayas%20Appliance%20Presence%20(Percentage%20of%20Buildings)%22%7D%7D%7D%7D)

### **Data Preprocessing**

Before conducting our experiments, we applied a series of preprocessing steps to ensure data quality and consistency across all datasets. This included handling missing values, removing erroneous or incomplete appliance records, and aligning timestamps to the desired temporal resolutions (15, 30, and 60 minutes). For datasets with higher frequency readings, we aggregated the measurements to the target intervals using appropriate statistical functions (e.g., mean or sum, depending on the appliance/load type). Additionally, we normalized appliance power consumption values to account for differences in measurement units and scales across datasets. In cases where appliance labels were not standardized, we performed label harmonization to ensure uniform category naming across datasets. For some datasets (e.g., ComStock and ResStock), we selected only a representative subset due to space constraints, and for restricted datasets (e.g., CER), we retained only the accessible portion while preserving the overall appliance category distribution.






