# Using Historical Demand, Weather, Calendar, and Macroeconomic Data to predict Future Daily Electricity Demand in Kenya

<img width="1536" height="1024" alt="demand forecasting" src="https://github.com/user-attachments/assets/74e58cfd-f072-4eb0-bcd5-474655daa7f7" />

--
## 1. Business Understanding
Electricity demand forecasting is a critical component of power system planning, grid reliability, and energy policy formulation. Kenya’s electricity demand has been growing steadily due to population growth, urbanization, and industrial expansion, while supply planning is increasingly complicated by climate variability and renewable energy integration. Accurate short-term demand forecasts are therefore essential to support operational efficiency and long-term infrastructure investment.
This project applies machine learning techniques to forecast daily national electricity demand (GWh) in Kenya using historical demand data combined with weather, calendar, and macroeconomic indicators. The work is situated within the energy systems and utilities domain, and the primary stakeholders include electricity utilities, system operators, energy regulators, policymakers, and investors. If deployed in practice, the model could improve load forecasting accuracy, reduce the risk of load shedding, optimize generation scheduling, and support evidence-based energy planning. The project builds on established load forecasting literature demonstrating that electricity demand is strongly influenced by seasonality, weather conditions, and long-term economic trends.

## 2. Data Understanding
## Data Sources and structure: 
The dataset is a consolidated national-level daily time series covering January 2022 to June 2024, stored as a CSV file. 
### The target variable is: 
 demand_gwh_daily: Daily national electricity demand (GWh)
 
### Explanatory variables include:
Weather variables: temperature, rainfall, humidity (synthetic but realistic)
Calendar features: date, weekday, weekend indicator, season
Macroeconomic indicators: GDP, population
The dataset contains 2,191 daily observations and 21 variables. The dataset is publicly accessible

## 3. Data Preparation 

Data Cleaning
Converted the date column to date time format and sorted observations chronologically.
Verified the absence of duplicate records.
Identified missing values primarily in forecast uncertainty columns, which were excluded from modeling.
Stripped column name whitespace and standardized formats.

## 4. Feature Engineering

To prepare the data for time-series–aware machine learning models, several features were engineered:
Calendar features: day, week of year, day of year
Cyclical encoding: sine and cosine transformations of month and weekday
Binary indicators: weekend vs weekday

### Leakage Prevention 
Aggregated demand variables derived from the target were removed to prevent target leakage.

---

## 5. Feature Selection 
Rationale
Feature selection balanced domain knowledge, statistical relevance, and methodological rigor. 
Features were chosen to capture short-term variability, seasonal structure, and long-term demand drivers while avoiding redundant or leakage-prone variables.
Final Feature Set included:
1. Calendar and seasonal indicators
2. Weather variables (temperature, rainfall, humidity)
3. GDP and population (long-term trend capture)

Excluded:
 Aggregated or target-derived demand metrics
 Static geographic identifiers
 Forecast uncertainty bound


5. Time-Series–Aware Train/Test Split


## 6. Modeling


### Supervised regression.



---

## Next Recommended Step





