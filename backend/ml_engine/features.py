import pandas as pd
import numpy as np

def build_features(csv_path):
    df = pd.read_csv(csv_path)
    df['dt'] = pd.to_datetime(df['dt'])
    df['year'] = df['dt'].dt.year
    df['month'] = df['dt'].dt.month

    df = df.dropna()

    df['temp_anomaly'] = df['LandAverageTemperature'] - df['LandAverageTemperature'].rolling(12).mean()

    df['trend_12m'] = df['LandAverageTemperature'].rolling(12).mean()
    df['trend_24m'] = df['LandAverageTemperature'].rolling(24).mean()

    df['risk_signal'] = np.where(df['temp_anomaly'] > 1.5, 2,
                          np.where(df['temp_anomaly'] > 0.8, 1, 0))

    return df.dropna()
