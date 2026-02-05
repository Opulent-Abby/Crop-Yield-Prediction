import joblib
import pandas as pd

FEATURES_PATH = '../models/feature_list.pkl'


def load_feature_list(path=FEATURES_PATH):
    try:
        features = joblib.load(path)
        return features
    except Exception:
        # fallback to common baseline
        return ['year', 'area_harvested_ha']


def preprocess(input_df):
    """Return a DataFrame with columns matching training features in the same order."""
    features = load_feature_list()
    df = pd.DataFrame(input_df)
    # ensure numeric types
    for c in features:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')
        else:
            df[c] = 0
    return df[features]
