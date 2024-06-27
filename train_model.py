import numpy as np
import pandas as pd
import io
import datetime
import pickle

from sklearn.metrics import mean_squared_error
from math import sqrt

from statsmodels.tsa.arima.model import ARIMA

from matplotlib import pyplot as plt

def process_per_category(df_full, category):
    df = df_full[df_full['JAHR'] <= 2021]
    df = df[df['MONATSZAHL'] == category]
    df = df[df['AUSPRAEGUNG'] == 'insgesamt']
    df = df[df['MONAT'] != 'Summe']

    df['PERIOD'] = pd.to_datetime(df['MONAT'], format='%Y%m')
    df = df.sort_values(by='PERIOD')

    return df

def train_model(train_data, model_name='ARIMA', savefile='forecast.pkl'):
    history = train_data['WERT']
    if model_name == 'ARIMA':
        model = ARIMA(history, order=(5,1,7))
    else:
        raise ValueError(f'Model name {model_name} not implemented')
    forecast_model = model.fit()
    pickle.dump(forecast_model, open(savefile, 'wb'))
    return forecast_model

def predict(model, forecast_len):
    y_pred = model.get_forecast(forecast_len)
    y_pred_model = y_pred.conf_int(alpha=0.05)
    y_pred_model['Predictions'] = model.predict(start=y_pred_model.index[0], end=y_pred_model.index[-1])
    return y_pred_model

if __name__ == "__main__":
    orig = pd.read_csv('data.csv')
    df = process_per_category(orig, 'Alkoholunfälle')
    train = df[df['PERIOD'] < pd.to_datetime("2020-01-01", format='%Y-%m-%d')]
    test = df[df['PERIOD'] >= pd.to_datetime("2020-01-01", format='%Y-%m-%d')]

    forecast_model = train_model(train)

    forecast = predict(forecast_model, len(test))
    rmse = sqrt(mean_squared_error(test['WERT'], forecast["Predictions"]))
    print(rmse)

