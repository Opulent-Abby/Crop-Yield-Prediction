# A Comparative Study of Ensemble Models for Crop Yield and Production Prediction in Kenya

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/2cc0db2f-1a07-4d94-9482-7cc31c41b579" />

## 1.0 Business Understanding
Agricultural production in Kenya is highly sensitive to climatic variability, land-use dynamics, and long-term structural transformation. Reliable prediction of crop production is therefore critical for food security planning, early warning systems, and evidence-based agricultural policy formulation.
This project evaluates the performance of baseline statistical models and ensemble machine learning methods in predicting crop production in Kenya, with particular attention to methodological rigor, temporal structure, and avoidance of target leakage.

## 2.0 Data Understanding

### 2.1 Data Source
The dataset is sourced from FAOSTAT and contains annual observations of crops and livestock products in Kenya from 1961 to 2021. The raw dataset includes 18,182 records and 14 variables, covering multiple agricultural elements such as production, harvested area, yield, and animal-related indicators.

Key fields include:
1. Crop item
2. Year
3. Element type (Production, Area harvested, Yield)
4. Unit of measurement
5. Observed value
6. Data quality flags (official, estimated, imputed, unofficial)

### 2.2 Scope of the Analysis
This project focuses exclusively on crop production, retaining only the following elements:
1. Total Production (tonnes)
2. Area harvested (hectares)
3. Yield (hectograms per hectare)

Animal-related variables were excluded due to a lot of missing values

The dataset captures long-term trends in:
1. Agricultural intensification
2. Policy shifts
3. Technological change
4. Climatic variability

## 3.0 Data Cleaning 
The following steps were applied to ensure data quality and analytical robustness:

1. Selection of Relevant Variables
2. Handling Missing and Inconsistent Values
3. Standardization
4. Renaming of Variables
5. Filtering based on data availability and reliability
6. Construction of time-ordered panel structures
7. Outlier assessment and diagnostics
8. Retained crop-related elements only
9. Enforced consistent units:
    - Production → tonnes
    - Area harvested → hectares
    - Yield → hg/ha
10. Converted data types and removed invalid or missing records
11. Normalized categorical text fields

 ## 3.1 Feature Engineering
 
### 3.2 Panel Construction
The dataset was reshaped from long to wide format, producing one row per:
1. Crop (item)
2. Year (Time-Series)

Core variables:
1. production_t
2. area_harvested_ha
3. yield_hg_per_ha

Missing yields were derived when both production and harvested area were available:

​<img width="500" height="87" alt="image" src="https://github.com/user-attachments/assets/5cf1ad73-bbe7-4a24-8c4b-5df9f431f91b" />

Yields were converted to tonnes per hectare.

### 3.3 Time-Based Feature Engineering

The following features were created:
1. Lagged variables (1–3 years)
2. Moving averages (3-year and 5-year)
3. Year-over-year growth rates
4. Normalized time trend

Outlier indicators
1. One-hot encoded flag classes
The final modeling dataset contains 5,764 rows across 139 crops.

## 4.0 Exploratory Data Analysis

## 4.1 Long-Term Yield Growth and Structural Change

<img width="497" height="278" alt="image" src="https://github.com/user-attachments/assets/539366b8-c721-4363-9ed9-3fa706b8047f" />

Canonical yield (t/ha) and 5-year moving average for Crop A, showing long-term productivity growth with substantial interannual variability.

## 4.2 Yield Volatility and Agricultural Risk
<img width="494" height="278" alt="image" src="https://github.com/user-attachments/assets/d54b9c0c-d3f6-40ed-9f94-c4041d9dcbfc" />

Canonical yield (t/ha) and 5-year moving average for Crop B, illustrating yield volatility, structural breaks, and gradual recovery over time.

## 4.3 Relationship between Harvest Area and Production
<img width="567" height="470" alt="image" src="https://github.com/user-attachments/assets/a69862ec-fdd2-458d-91b7-a998c091be8d" />

Figure 3.0 (Scatter plots of Area vs. Production) confirm strong positive but non-linear relationships among the key agricultural variables.
## 4.4 Relationship between Yield and Production
<img width="567" height="455" alt="image" src="https://github.com/user-attachments/assets/744d572f-2bd9-46e5-a73b-1e2d318418bd" />

Figures 4(Scatter plots of Yield vs. Production) confirm strong positive but non-linear relationships among the key agricultural variables. 

## 5.0 Modeling Approach

### 5.1 Model Design Principles: 
1. Leakage-free feature selection
2. Time-aware train–test splitting
3. Comparison of linear and non-linear learners
4. Regularization to control overfitting
5. Evaluation using multiple performance metrics

### 5.2 Linear Regression Baseline (Ordinary least squares)

| Metric         | Value     |
| ---------------| --------- |
| MAE            | 189,411 t |
| RMSE           | 314,468 t |
| R²             | 0.596     |

The linear model captures broad temporal trends but is limited in modeling non-linear relationships.

### 5.3 Random Forest Regression

| Metric         | Training Set     | Test Set  |
| ------------   | ---------------- | --------- |
| MAE            | 120,817 t        | 118,577 t |
| RMSE           | 395,795 t        | 347,582 t |
| R²             | 0.6051           | 0.5070    |

### Feature Importance:

| Feature                     | Importance |
| ----------------------------| ---------- |
| area_harvested_ha           | 88.8%      |
| year                        | 11.2%      |

The Random Forest captures non-linear interactions while maintaining generalization under leakage-free constraints.

### 5.4 XGBoost Regression
An XGBoost model was trained using identical predictors and regularization to prevent overfitting.

| Metric           | Value     |
| -----------------| --------- |
| MAE              | 115,432 t |
| RMSE             | 332,985 t |
| R²               | 0.512     |

<img width="477" height="278" alt="image" src="https://github.com/user-attachments/assets/62e91343-d2a7-4930-bb26-afc0859efa7a" />
Performance is comparable to Random Forest, indicating robustness of ensemble methods under constrained feature spaces.

## 6.0 Model Evaluation and Interpretation

| Model                 | Test R² | MAE (t) | RMSE (t) | Remarks                                        |
| --------------------- | ------- | ------- | -------- | ---------------------------------------------- |
| Linear Regression     | 0.596   | 189,411 | 314,468  | Baseline linear trend captured                 |
| Random Forest (Final) | 0.507   | 118,577 | 347,582  | Non-linear interactions captured; leakage-free |
| XGBoost               | 0.512   | 115,432 | 332,985  | Similar performance to RF; robust              |

   Key Insights:
1. Ensemble models outperform the linear baseline in capturing non-linearities and interactions
2. Harvested area is the dominant driver of production, with temporal trends captured via year
3. Leakage-free modeling substantially reduces apparent performance but improves real-world validity
4. Predictive power is constrained by limited covariates; incorporation of climate, fertilizer use, soil quality, and policy variables would likely improve forecasts

## 7.0 Final Model Selection

The Random Forest (leakage-free, regularized) model is selected as the final model due to its:
1. Stability
2. Interpretability
3. Robust out-of-sample performance
4. Strict avoidance of target leakage


