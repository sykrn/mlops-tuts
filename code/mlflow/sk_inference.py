import mlflow
import mlflow.sklearn
import numpy as np
from sklearn import datasets

# Load Iris dataset
iris = datasets.load_iris()

# Ambil model dari MLflow
model_uri = "runs:/<RUNID>/model"  # Ganti <RUN_ID> dengan ID run yang sesuai
model = mlflow.sklearn.load_model(model_uri)

# Contoh data baru untuk melakukan prediksi
# Misalnya kita ingin memprediksi data iris dengan sepal length=5.0, sepal width=3.5, petal length=1.5, petal width=0.2
new_data = np.array([[5.0, 3.5, 1.5, 0.2]])

# Melakukan inference
predicted_class = model.predict(new_data)
print(predicted_class)

# Mengambil nama kelas dari target
class_names = iris.target_names
predicted_class_name = class_names[predicted_class][0]

print(f"Predicted class: {predicted_class_name} (Predicted label: {predicted_class[0]})")
