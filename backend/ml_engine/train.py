import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib
from features import build_features

df = build_features("../../data/GlobalTemperatures.csv")

X = df[['year','month','trend_12m','trend_24m','temp_anomaly']]
y = df['risk_signal']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = XGBClassifier(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.9,
    colsample_bytree=0.9
)

model.fit(X_train,y_train)

joblib.dump(model,"climate_risk_model.pkl")

print("Model Trained Successfully")
