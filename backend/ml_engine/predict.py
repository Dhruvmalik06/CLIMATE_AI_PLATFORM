import joblib
import pandas as pd

model = joblib.load("ml_engine/climate_risk_model.pkl")

def predict_climate_risk(year, month, trend12, trend24, anomaly):

    X = pd.DataFrame([[year, month, trend12, trend24, anomaly]],
        columns=['year','month','trend_12m','trend_24m','temp_anomaly'])

    pred = int(model.predict(X)[0])
    proba = model.predict_proba(X)[0].tolist()

    return {
        "class": pred,
        "probabilities": proba
    }
