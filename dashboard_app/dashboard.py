import streamlit as st
import pandas as pd
import joblib
import os
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title='Kenya Crop Yield Dashboard', layout='wide')

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'final_model.joblib')
FEATURES_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'feature_list.pkl')

st.title('Kenya Crop Yield — Interactive Dashboard')

# Load model
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        st.error(f'Error loading model: {e}')
else:
    st.warning('No trained model found. Run `python export_model.py` to train and export the model.')

# Sidebar controls
st.sidebar.header('Prediction Input')
year = st.sidebar.number_input('Year', min_value=2000, max_value=2050, value=2025)
area = st.sidebar.number_input('Area harvested (ha)', min_value=0.0, value=10000.0)

st.sidebar.header('Scenario')
area_change = st.sidebar.slider('Area change (%)', -20, 20, 0)

# Predict
if model is not None:
    input_df = pd.DataFrame([{'year': year, 'area_harvested_ha': area}])
    try:
        pred = model.predict(input_df)[0]
        st.metric('Predicted production (tonnes)', f'{pred:,.0f}')
    except Exception as e:
        st.error(f'Prediction error: {e}')

    # Scenario projection table
    st.subheader('Scenario Projection (2026-2030)')
    baseline = input_df.copy()
    years = list(range(2026, 2031))
    rows = []
    med_area = area
    for y in years:
        rows.append({'year': y, 'area_harvested_ha': med_area})

    X_future = pd.DataFrame(rows)
    preds_base = model.predict(X_future)

    X_scen = X_future.copy()
    X_scen['area_harvested_ha'] = X_scen['area_harvested_ha'] * (1 + area_change/100.0)
    preds_scen = model.predict(X_scen)

    df_proj = pd.DataFrame({'year': years, 'baseline': preds_base, 'scenario': preds_scen})
    st.line_chart(df_proj.set_index('year'))

    st.write('Projection table')
    st.dataframe(df_proj)
else:
    st.info('Train and export a model to enable predictions and projections.')

# Show evaluation artifacts if present
st.sidebar.header('Evaluation')
if os.path.exists('models/metrics.json'):
    metrics = pd.read_json('models/metrics.json', typ='series')
    st.sidebar.write(metrics)

st.sidebar.markdown('---')
st.sidebar.write('Run export_model.py to (re)train and export the model.')
