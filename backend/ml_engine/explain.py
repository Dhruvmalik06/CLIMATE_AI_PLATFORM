import shap
import joblib
import pandas as pd

model = joblib.load("climate_risk_model.pkl")

explainer = shap.TreeExplainer(model)

def explain_prediction(X):
    shap_values = explainer.shap_values(X)
    return shap_values
