# A Comparative Study of Ensemble Models for Crop Yield and Production Prediction in Kenya

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/b39c77c0-7a2e-461f-8b7d-3071e7b1e161" />

## Business Understanding
Agricultural production in Kenya is highly sensitive to climatic variability, land-use dynamics, and long-term structural change. Accurate prediction of crop yields and production is therefore essential for food security planning and agricultural policy formulation.


<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/2cc0db2f-1a07-4d94-9482-7cc31c41b579" />


## Data Understanding
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

## Data Cleaning

## Exploratory Data Analysis

## Long-Term Yield Growth and Structural Change

<img width="497" height="278" alt="image" src="https://github.com/user-attachments/assets/539366b8-c721-4363-9ed9-3fa706b8047f" />

Canonical yield (t/ha) and 5-year moving average for Crop A, showing long-term productivity growth with substantial interannual variability.

## Yield Volatility and Agricultural Risk
<img width="494" height="278" alt="image" src="https://github.com/user-attachments/assets/d54b9c0c-d3f6-40ed-9f94-c4041d9dcbfc" />

Canonical yield (t/ha) and 5-year moving average for Crop B, illustrating yield volatility, structural breaks, and gradual recovery over time.

## Modeling Approach


