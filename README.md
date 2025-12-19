# Using historical demand, weather, calendar, and macroeconomic data, can we predict future daily electricity demand in Kenya?
--
## 1. Business Understanding (ADD / REFINE)
Electricity demand forecasting is critical for power system planning and grid reliability. This project uses daily national electricity demand data from Kenya, combined with weather, calendar, and macroeconomic indicators, to predict future electricity demand. The final model captures seasonal and weather-driven demand patterns and provides a realistic forecasting tool for energy planners.
## Rationale (business value)
This prediction is valuable for:
   ###  1. Power system planning and grid stability
   ###  2. Load forecasting for utilities and energy regulators
   ###  3. Reducing generation shortfalls and excess capacity costs

**Problem Statement**
Accurately forecasting daily national electricity demand in Kenya using historical demand, weather, calendar, and macroeconomic variables.

**Why This Topic Matters**
Electricity demand forecasting supports grid reliability, generation planning, and cost-efficient energy policy in fast-growing economies.

**Domain / Industry**
Energy systems, power utilities, and public-sector energy planning.

**Target Audience**
Energy utilities, system operators, regulators, and policy planners.

**Real-World Impact**
Improved forecasts can reduce load-shedding risk, optimize generation scheduling, and inform long-term infrastructure investment.

**Domain Knowledge / Prior Work**
The project builds on established load-forecasting literature showing that demand is driven by weather, seasonality, and economic growth.

👉 **Action**: Add this as a Markdown section at the top of your notebook.

---

## 2. Data Understanding 

* Data source and structure
* Variable types and ranges
* Missing values
* Demand trends and seasonality
* Weather and macroeconomic relationships

**What to Explicitly Add**:

* Data source citation (ERA5 for weather, World Bank for GDP/population)
* Statement that data is **daily, national-level, 2022–2027**

👉 **Action**: Add a short Markdown paragraph summarizing data provenance.

---

## 3. Data Preparation (GOOD — NEEDS STRUCTURE & JUSTIFICATION)

### Storage & Types

* CSV file, mixed numeric and categorical variables
* Daily time index

### Cleaning Steps (ALREADY DONE)

* Date parsing and sorting
* Duplicate check
* Column name normalization

### Missing Values

* Demand interval bounds contain ~33% missing values
* These columns were excluded to avoid introducing bias

### Feature Engineering (STRONG)

* Calendar features (day, week, day of year)
* Cyclical encoding (month, weekday)
* Weather variables
* Macroeconomic variables

### Leakage Prevention (IMPORTANT — ADD TEXT)

Aggregated demand variables derived from the target were removed to prevent target leakage.

👉 **Action**: Add Markdown headings explaining *why* each step was done.

---

## 4. Feature Selection (ADD A SHORT JUSTIFICATION)

**Rationale**
Features were selected to balance domain relevance, statistical signal, and leakage prevention.

**Final Features Include**:

* Calendar and seasonal indicators
* Weather variables
* GDP and population (long-term trend capture)

**Excluded**:

* Aggregated or derived demand metrics
* Static geographic identifiers

👉 **Action**: Add a brief Markdown explanation before `df_model`.

---

## 5. Time-Series–Aware Train/Test Split (MUST ADD)

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

👉 **Action**: Add a Markdown cell explaining leakage prevention.

---

## 6. Modeling (NEXT STEP — REQUIRED)

### Problem Type

Supervised **regression**.

### Target Variable

`demand_gwh_daily`

### Baseline Model (REQUIRED)

* Naive baseline (yesterday = today) **or**
* Linear Regression

### Final Model (RECOMMENDED)

* Random Forest Regressor
* Gradient Boosting / XGBoost (optional level-up)

👉 **Action**: Implement baseline first, then one tree-based model.

---

## 7. Evaluation (ADD CLEAR METRICS)

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

👉 **Action**: Add a table comparing model performance.

---

## 8. Deployment (LIGHTWEIGHT — CONCEPTUAL ONLY)

**Reporting**
Results reported via plots, metrics, and feature importance charts.

**Deployment Concept**
Model could be deployed as a forecasting API or dashboard for planners.

👉 **Action**: Add a short Markdown section (no app required).

---

## 9. Tools & Methodologies (ADD SUMMARY CELL)

* Python (pandas, numpy)
* Visualization (matplotlib, seaborn)
* Modeling (scikit-learn)
* Local Jupyter Notebook environment


<img width="1536" height="1024" alt="demand forecasting" src="https://github.com/user-attachments/assets/74e58cfd-f072-4eb0-bcd5-474655daa7f7" />
---

### Next Recommended Step

Implement the **baseline model and evaluation** — this unlocks the rest of the Capstone.





