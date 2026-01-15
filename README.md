# A Comparative Study of Ensemble Models for Crop Yield and Production Prediction in Kenya

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/2cc0db2f-1a07-4d94-9482-7cc31c41b579" />

## 1.0 Business Understanding
Agricultural production in Kenya is highly sensitive to climatic variability, land-use dynamics, and long-term structural change. Accurate prediction of crop yields and production is therefore essential for food security planning and agricultural policy formulation.

## 2.0 Data Understanding
This project applies and compares baseline statistical models and ensemble machine-learning approaches to predict crop production in Kenya using long-term FAOSTAT panel data (1961–2021). Particular emphasis is placed on avoiding target leakage, handling temporal non-stationarity, and evaluating model generalizability using out-of-sample performance.
### Crop type
1. Harvested area (hectares)
2. Yield (tonnes per hectare)
3. Total production (tonnes)

The dataset spans multiple decades, capturing:
1. Structural changes in agricultural systems
2. Policy shifts
3. Climatic and technological variability

A key challenge in this data is that production is mechanically derived from yield and harvested area, which creates a high risk of target leakage if features are not handled carefully.

## 3.0 Data Cleaning

The following steps were applied:

1. Selection of Relevant Variables
2. Handling Missing and Inconsistent Values
3. Standardization and Renaming of Variables
4. Filtering Based on Data Quality
5. Construction of Time Series
6. Outlier Assessment
7. Feature Transformation and Engineering


## 4.0 Exploratory Data Analysis

## Long-Term Yield Growth and Structural Change

<img width="497" height="278" alt="image" src="https://github.com/user-attachments/assets/539366b8-c721-4363-9ed9-3fa706b8047f" />

Canonical yield (t/ha) and 5-year moving average for Crop A, showing long-term productivity growth with substantial interannual variability.

## Yield Volatility and Agricultural Risk
<img width="494" height="278" alt="image" src="https://github.com/user-attachments/assets/d54b9c0c-d3f6-40ed-9f94-c4041d9dcbfc" />

Canonical yield (t/ha) and 5-year moving average for Crop B, illustrating yield volatility, structural breaks, and gradual recovery over time.

## Relationship between Harvest Area and Production
<img width="567" height="470" alt="image" src="https://github.com/user-attachments/assets/a69862ec-fdd2-458d-91b7-a998c091be8d" />

Figure 3.0 (Scatter plots of Area vs. Production) confirm strong positive but non-linear relationships among the key agricultural variables.
## Relationship between Yield and Production
<img width="567" height="455" alt="image" src="https://github.com/user-attachments/assets/744d572f-2bd9-46e5-a73b-1e2d318418bd" />

Figures 4(Scatter plots of Yield vs. Production) confirm strong positive but non-linear relationships among the key agricultural variables. 

## 5.0 Modeling Approach

### 5.1 Linear Regression Baseline (Ordinary least squares)

| Metric | Value     |
| ------ | --------- |
| MAE    | 189,411 t |
| RMSE   | 314,468 t |
| R²     | 0.596     |

### 5.2 Random Forest Regression

| Metric | Training Set | Test Set  |
| ------ | ------------ | --------- |
| MAE    | 120,817 t    | 118,577 t |
| RMSE   | 395,795 t    | 347,582 t |
| R²     | 0.6051       | 0.5070    |

### Feature Importance:

| Feature           | Importance |
| ----------------- | ---------- |
| area_harvested_ha | 88.8%      |
| year              | 11.2%      |

### 5.3 XGBoost Regression
An XGBoost model was trained using the same predictors for comparison. 
The model was configured with regularization to prevent overfitting.

| Metric | Value     |
| ------ | --------- |
| MAE    | 115,432 t |
| RMSE   | 332,985 t |
| R²     | 0.512     |

<img width="477" height="278" alt="image" src="https://github.com/user-attachments/assets/62e91343-d2a7-4930-bb26-afc0859efa7a" />

## 6.0 Model Evaluation and Interpretation

| Model                 | Test R² | MAE (t) | RMSE (t) | Remarks                                        |
| --------------------- | ------- | ------- | -------- | ---------------------------------------------- |
| Linear Regression     | 0.596   | 189,411 | 314,468  | Baseline linear trend captured                 |
| Random Forest (Final) | 0.507   | 118,577 | 347,582  | Non-linear interactions captured; leakage-free |
| XGBoost               | 0.512   | 115,432 | 332,985  | Similar performance to RF; robust              |

Key Insights:
1. Regularized Random Forest and XGBoost models outperform the linear regression baseline in handling non-linearities and interactions.
2. The dominant driver of production is harvested area, with temporal trends captured by year.
3. Models are limited by available predictors; additional variables such as climate, fertilizer use, or soil quality would likely improve predictive power.
4. Final model selection is the Random Forest (leakage-free, regularized), due to its stability, interpretability, and absence of target leakage.



