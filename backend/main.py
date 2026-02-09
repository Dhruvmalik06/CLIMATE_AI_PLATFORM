from fastapi import FastAPI
import joblib
import pandas as pd
from ml_engine.risk_engine import risk_reasoning

app = FastAPI()

model = joblib.load("ml_engine/climate_risk_model.pkl")

@app.get("/predict")
def predict(year:int, month:int, t12:float, t24:float, anomaly:float):

    X = pd.DataFrame([[year,month,t12,t24,anomaly]],
                     columns=['year','month','trend_12m','trend_24m','temp_anomaly'])

    pred = int(model.predict(X)[0])

    risk = risk_reasoning(pred, X.to_dict())

    return {"prediction":pred,"risk":risk}
