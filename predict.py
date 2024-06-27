import requests
import json

# Input data
input_data_json = json.dumps({"year": "2021", "month": "01"})

# endpoint
scoring_uri = 'http://4ac29a78-1148-4042-a9dd-0f66273e04c2.northeurope.azurecontainer.io/score'

# Define the content type
headers = {"Content-Type": "application/json"}

# Send an HTTP POST request to the endpoint
response = requests.post(scoring_uri, data=input_data_json, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    result = json.loads(response.json())

    # Extract the prediction (result) from the response
    prediction = result["Prediction"]
    print(f"Prediction: {prediction}")
else:
    print(f"Error: {response.text}")