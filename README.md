# A Comparative Study of Ensemble Models for Crop Yield and Production Prediction in Kenya

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/2cc0db2f-1a07-4d94-9482-7cc31c41b579" />

## 1.0 Business Understanding
Agricultural production in Kenya is highly sensitive to climatic variability, land-use dynamics, and long-term structural transformation. Reliable prediction of crop production is therefore critical for food security planning, early warning systems, and evidence-based agricultural policy formulation.

## 2.0 Data Understanding

### 2.1 Data Source
This project applies and compares baseline statistical models and ensemble machine-learning approaches to predict crop production in Kenya using long-term FAOSTAT panel data (1961–2021). Particular emphasis is placed on avoiding target leakage, handling temporal non-stationarity, and evaluating model generalizability using out-of-sample performance.

### 2.2 Crop Variable
1. Harvested area (hectares)
2. Yield (tonnes per hectare)
3. Total production (tonnes)
The dataset spans multiple decades, capturing:
1. Structural changes in agricultural systems
2. Policy shifts
3. Climatic and technological variability

### 2.3 Key Methodological Challenge: Target Leakage

Agricultural production is mechanically defined as:

Production = Harvested Area × Yield

Including yield as a predictor when forecasting production introduces severe target leakage, artificially inflating model performance. This project explicitly identifies, diagnoses, and corrects for leakage by restricting predictors to causally and temporally valid features.

## 3.0 Data Cleaning and Preprocessing
The following steps were applied to ensure data quality and analytical robustness:

1. Selection of Relevant Variables
2. Handling Missing and Inconsistent Values
3. Standardization and Renaming of Variables
4. Filtering based on data availability and reliability
5. Construction of time-ordered panel structures
6. Outlier assessment and diagnostics
7. Feature transformation and basic feature engineering

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


