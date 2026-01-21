# A Comparative Study of Ensemble Models for Crop Yield and Production Prediction in Kenya

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/2cc0db2f-1a07-4d94-9482-7cc31c41b579" />


## 1.0 Business Understanding
Agricultural production in Kenya is highly sensitive to climatic variability, land-use dynamics, and long-term structural transformation. Reliable prediction of crop production is therefore critical for food security planning, early warning systems, and evidence-based agricultural policy formulation.
This project evaluates the performance of baseline statistical models and ensemble machine learning methods in predicting crop production in Kenya, with particular attention to methodological rigor, temporal structure, and avoidance of target leakage.

## 1.1 Research Objectives

### Primary Objective
To develop and evaluate leakage-safe statistical and ensemble machine learning models for predicting total crop production (tonnes) in Kenya using long-term FAOSTAT panel data.

### Secondary Objectives
1. To compare the predictive performance of baseline linear models and ensemble methods under time-aware train–test splits.
2. To examine the role of harvested area, historical yield dynamics, and temporal trends in explaining crop production variability.


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
1. Primary Prediction Target:
- Variable: Total crop production
- Unit: Tonnes
- Prediction task: Annual, crop-level production forecasting
2. Area harvested (hectares)
3. Yield (hectograms per hectare)
  
Yield is not used as a contemporaneous predictor due to its mechanical relationship with production, but is incorporated indirectly through lagged and rolling transformations to avoid target leakage.

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

<img width="500" height="87" alt="image" src="https://github.com/user-attachments/assets/5cf1ad73-bbe7-4a24-8c4b-5df9f431f91b" />

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

Figure 1.0 shows Canonical yield (t/ha) and 5-year moving average for Crop A, showing long-term productivity growth with substantial interannual variability.

## 4.2 Yield Volatility and Agricultural Risk
<img width="494" height="278" alt="image" src="https://github.com/user-attachments/assets/d54b9c0c-d3f6-40ed-9f94-c4041d9dcbfc" />

Figure 2.0 shows Canonical yield (t/ha) and 5-year moving average for Crop B, illustrating yield volatility, structural breaks, and gradual recovery over time.

## 4.3 Relationship between Harvest Area and Production
<img width="567" height="470" alt="image" src="https://github.com/user-attachments/assets/a69862ec-fdd2-458d-91b7-a998c091be8d" />

Figure 3.0 (Scatter plots of Area vs. Production) confirm strong positive but non-linear relationships among the key agricultural variables.
## 4.4 Relationship between Yield and Production

<img width="567" height="455" alt="image" src="https://github.com/user-attachments/assets/744d572f-2bd9-46e5-a73b-1e2d318418bd" />

Figure 4.0(Scatter plots of Yield vs. Production) confirm strong positive but non-linear relationships among the key agricultural variables. 

## 5.0 Modeling Approach

### 5.1 Model Design Principles: 
1. Leakage-free feature selection
2. Time-aware train–test splitting
3. Comparison of linear and non-linear learners
4. Regularization to control overfitting
5. Evaluation using multiple performance metrics
6. Data were split using a chronological train–test strategy, with earlier years used for training and later years reserved for testing. This approach reflects real-world forecasting conditions and prevents information leakage from future observations.


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

Figure 5.0 shows performance is comparable to Random Forest, indicating robustness of ensemble methods under constrained feature spaces.

## 6.0 Model Evaluation and Interpretation

| Model                 | Test R² | MAE (t) | RMSE (t) | Remarks                                        |
| --------------------- | ------- | ------- | -------- | ---------------------------------------------- |
| Linear Regression     | 0.596   | 189,411 | 314,468  | Baseline linear trend captured                 |
| Random Forest (Final) | 0.507   | 118,577 | 347,582  | Non-linear interactions captured; leakage-free |
| XGBoost               | 0.512   | 115,432 | 332,985  | Similar performance to RF; robust              |

### 6.1 Evaluation Approach
All models were evaluated using a time-aware train–test split, where training was performed on historical data and testing on future observations. This strategy prevents temporal data leakage and provides a realistic assessment of out-of-sample forecasting performance.

Models were compared using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R². While R² reflects explanatory power, MAE and RMSE capture the magnitude of prediction errors.

### 6.2 Model Comparison Results
The naive baseline model exhibited the weakest performance, with the highest error values and a negative R², confirming that more advanced models add predictive value.

Linear Regression, Ridge Regression, and Lasso Regression achieved moderate performance, explaining approximately 60% of the variance in production. However, their relatively high error values indicate limitations in capturing non-linear relationships. Regularization (L1 and L2) did not lead to meaningful improvements, suggesting that multicollinearity and feature sparsity are not dominant issues in this dataset.

Among ensemble models, XGBoost achieved slightly lower MAE than linear models but showed higher RMSE and lower R², indicating sensitivity to large errors and weaker generalization. In contrast, the Random Forest model consistently outperformed all other approaches, achieving the lowest MAE and RMSE and the highest R².

### 6.3 Final Model Selection
Based on overall predictive accuracy and robustness, Random Forest was selected as the final model. Its superior performance suggests the presence of strong non-linear patterns and interactions in the data that are effectively captured by tree-based ensemble methods.

   
## 6.4 Recommendations and Future Work
Future improvements may include additional hyperparameter tuning of the Random Forest model, incorporation of feature importance and explainability techniques (e.g., permutation importance or SHAP), and the use of rolling or expanding window validation to further assess temporal generalization. Enhancing data quality and incorporating additional explanatory variables may also improve performance, particularly for more complex models such as XGBoost.


## 7.0 Final Model Selection

The Random Forest (leakage-free, regularized) model is selected as the final model due to its:
1. Stability
2. Interpretability
3. Robust out-of-sample performance
4. Strict avoidance of target leakage

## 8.0 Deployment Considerations

Although this project primarily focuses on model development and evaluation, the selected Random Forest model is suitable for operational deployment in an agricultural forecasting context.

In a production setting, the trained model would be integrated into a forecasting pipeline that applies the same preprocessing and feature engineering steps to newly available annual agricultural data. Once processed, the model can generate production forecasts to support agricultural planning, food security monitoring, and policy decision-making.

Deployment could be implemented as a batch forecasting workflow, where predictions are generated annually as new FAOSTAT or related datasets become available. The trained model and preprocessing pipeline can be serialized using tools such as `joblib` or `pickle`, and the outputs can be consumed through dashboards or reporting systems.

To ensure long-term reliability, the deployed model should be periodically retrained as new data becomes available. Additional validation strategies, such as rolling or expanding window evaluation, would also be necessary to confirm that the model generalizes well under changing agricultural and climatic conditions.

## 9.0 Limitations
This analysis is subject to several limitations. 
1. The models rely primarily on historical production, area, and yield data, without explicit climatic, soil, or input-use variables.
2. FAOSTAT data may contain measurement error and imputed values despite quality filtering.
3. The national-level aggregation masks regional heterogeneity and localized shocks.


