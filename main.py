from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import numpy as np
from .preprocess import preprocess

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'final_model.joblib')

app = FastAPI(title='Kenya Crop Yield Predictor')

class PredictRequest(BaseModel):
    data: list

# Load model at startup
model = None
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None


@app.get('/')
def health():
    return {'status': 'ok', 'model_loaded': model is not None}


@app.post('/predict')
def predict(req: PredictRequest):
    if model is None:
        raise HTTPException(status_code=503, detail='Model not available. Run export_model.py first.')
    try:
        df_in = preprocess(req.data)
        preds = model.predict(df_in)
        return {'predictions': preds.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
