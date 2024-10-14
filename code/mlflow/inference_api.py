import requests
import numpy as np
import json

# Start Serving the Model: You can use the following command in your terminal (replace <RUN_ID> with your actual run ID):
# mlflow models serve -m runs:/2f3c242873fa4e9ea6085cbb9cc407bc/model -p 5000


# URL of the model
url = "http://127.0.0.1:5000/invocations"

# Example input data for prediction
data = {
    "columns": ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"],
    "data": [[5.0, 3.5, 1.5, 0.2]]
}

# Send POST request for prediction
response = requests.post(url, json=data)

# Print the predicted class
print("Predicted class:", response.json())
