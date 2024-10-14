# Import library yang dibutuhkan
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso, LogisticRegression
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
import os

# Mengaktifkan autolog, MLflow akan secara otomatis melacak semua parameter, metrik, dan model yang digunakan
mlflow.sklearn.autolog()

# Memuat dataset Iris
data = load_iris()
X = data.data  # Fitur
y = data.target  # Target (spesies bunga iris)

# Membagi dataset menjadi data latih (80%) dan data uji (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat folder untuk menyimpan artefak
os.makedirs("artefak", exist_ok=True)

# Fungsi untuk menjalankan eksperimen dengan model dan alpha yang berbeda
def run_experiment(model_name, C):
    with mlflow.start_run(run_name=model_name):  # Nama eksperimen sesuai dengan model
        # Inisialisasi model Ridge atau Lasso dengan nilai alpha
        if model_name == "Ridge":
            model = LogisticRegression(penalty='l2', solver='liblinear', random_state=42, C=C)
        elif model_name == "Lasso":
            model = LogisticRegression(penalty='l1', solver='liblinear', random_state=42, C=C)
            
        # Melatih model
        model.fit(X_train, y_train)
        
        # Prediksi dan evaluasi model
        predictions = model.predict(X_test)
        accuracy = (predictions == y_test).mean()
        
        # Membuat plot scatter prediksi vs target asli
        plt.figure(figsize=(6, 6))
        plt.scatter(y_test, predictions)
        plt.xlabel("Spesies Aktual")
        plt.ylabel("Spesies Prediksi")
        plt.title(f"Prediksi vs Aktual: {model_name} (C={C})")
        
        # Menyimpan plot sebagai artefak
        plot_path = f"artefak/{model_name}_C_{C}.png"
        plt.savefig(plot_path)
        mlflow.log_artifact(plot_path)  # Menyimpan plot sebagai artefak
        
        print(f"{model_name} dengan C={C} selesai")
        plt.close()

# Menjalankan eksperimen dengan Ridge dan Lasso menggunakan nilai alpha yang berbeda
for C in [0.1, 1.0, 10.0]:
    run_experiment("Ridge", C)
    run_experiment("Lasso", C)

# Jalankan `mlflow ui` di terminal untuk melihat hasil eksperimen
