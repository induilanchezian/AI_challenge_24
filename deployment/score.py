import json
#import joblib
import pickle
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path('accident_forecasting_model')
    # model = joblib.load(model_path)
    model = pickle.load(open(model_path, 'rb'))

def run(raw_data):
    try:
        year = json.loads(raw_data)['year']
        month = json.loads(raw_data)['month']

        num_years = int(year) - 2021
        n = int(month) + (12 * num_years)

        # Perform prediction using the loaded model
        y_pred = model.get_forecast(n)
        y_pred_model = y_pred.conf_int(alpha = 0.05)
        y_pred_model["Predictions"] = model.predict(start = y_pred_model.index[0], end = y_pred_model.index[-1])
        prediction = y_pred_model['Predictions'].tolist()[-1]

        return json.dumps({"Prediction": prediction})


    except Exception as e:
        return json.dumps({"error": str(e)})
