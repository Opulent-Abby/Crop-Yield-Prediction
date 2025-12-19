# Using historical demand, weather, calendar, and macroeconomic data, can we predict future daily electricity demand in Kenya?
--
## 1. Business Understanding
Electricity demand forecasting is critical for power system planning and grid reliability. This project uses daily national electricity demand data from Kenya, combined with weather, calendar, and macroeconomic indicators, to predict future electricity demand. The final model captures seasonal and weather-driven demand patterns and provides a realistic forecasting tool for energy planners.

## Rationale (business value)
This prediction is valuable for:
**Power system planning and grid stability**
**Load forecasting for utilities and energy regulators**
**Reducing generation shortfalls and excess capacity costs**

**Domain / Industry**
Energy systems, power utilities, and public-sector energy planning.
**Target Audience**
Energy utilities, system operators, regulators, and policy planners.
**Real-World Impact**
Improved forecasts can reduce load-shedding risk, optimize generation scheduling, and inform long-term infrastructure investment.
**Domain Knowledge / Prior Work**
The project builds on established load-forecasting literature showing that demand is driven by weather, seasonality, and economic growth.


**Procedure and Project Overview**
## Collecting the data

## Data Sources and structure: 
### Storage & Types
* CSV file, mixed numeric and categorical variables
* Daily time index

**Variables types and ranges**

**Data Cleaning and EDA**
Data Cleaning and EDA
- How were the missing values treated

**Demand trends and seasonality**

**Weather and macroeconomic relationships**

### Feature Engineering

* Calendar features (day, week, day of year)
* Cyclical encoding (month, weekday)
* Weather variables
* Macroeconomic variables

### Leakage Prevention 
Aggregated demand variables derived from the target were removed to prevent target leakage.

---

## 4. Feature Selection 
**Rationale**
Features were selected to balance domain relevance, statistical signal, and leakage prevention.

**Final Features Include**:

* Calendar and seasonal indicators
* Weather variables
* GDP and population (long-term trend capture)

**Excluded**:

* Aggregated or derived demand metrics
* Static geographic identifiers

---

## 5. Time-Series–Aware Train/Test Split 

### Why This Matters

Random splits leak future information in time-series forecasting.

### Implementation

* Train: 2022–2025
* Test: 2026–2027

```python
split_date = "2026-01-01"
train = df_model[df["date"] < split_date]
test  = df_model[df["date"] >= split_date]
```
---

**Results**

## 6. Modeling 

### Problem Type

Supervised **regression**.

### Target Variable

`demand_gwh_daily`

### Baseline Model 

* Naive baseline (yesterday = today) **or**
* Linear Regression

### Final Model (RECOMMENDED)

* Random Forest Regressor
* Gradient Boosting / XGBoost (optional level-up)

---

## 7. Evaluation 

### Metrics

* MAE (primary)
* RMSE
* R² (optional)

### Evaluation Strategy

* Evaluate only on future (test) data
* Compare baseline vs final model

### MVP Definition

A model that outperforms the baseline on MAE using a leakage-free time split.

### Stretch Goals

* Hyperparameter tuning
* Feature importance interpretation
* Error analysis by season

---

## 8. Deployment 

**Reporting**
Results reported via plots, metrics, and feature importance charts.

**Deployment Concept**
Model could be deployed as a forecasting API or dashboard for planners.

---


<img width="1536" height="1024" alt="demand forecasting" src="https://github.com/user-attachments/assets/74e58cfd-f072-4eb0-bcd5-474655daa7f7" />
---

### Next Recommended Step

Implement the **baseline model and evaluation** — this unlocks the rest of the Capstone.





