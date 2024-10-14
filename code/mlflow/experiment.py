# Import library yang dibutuhkan
import mlflow  # Untuk melacak eksperimen
import mlflow.sklearn  # Untuk mencatat dan menyimpan model scikit-learn
from sklearn.model_selection import train_test_split  # Untuk membagi dataset menjadi data latih dan uji
from sklearn.linear_model import LogisticRegression  # Model Regresi Logistik
from sklearn.datasets import load_iris  # Dataset Iris
from sklearn.metrics import accuracy_score  # Menghitung akurasi sebagai metrik
from mlflow.models import infer_signature

# Memuat dataset Iris
data = load_iris()
X = data.data  # Fitur
y = data.target  # Target (spesies bunga iris)

# Membagi dataset menjadi data latih (80%) dan data uji (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

mlflow.set_experiment("pilot experiment")

# Mulai pelacakan eksperimen dengan MLflow
with mlflow.start_run():
    # Inisialisasi model Regresi Logistik
    model = LogisticRegression(max_iter=200)
    
    # Melatih model menggunakan data latih
    model.fit(X_train, y_train)
    
    # Melakukan prediksi pada data uji
    predictions = model.predict(X_test)
    
    # Menghitung akurasi sebagai metrik evaluasi
    accuracy = accuracy_score(y_test, predictions)
    
    # Mencatat parameter model (apakah intercept digunakan dalam regresi)
    mlflow.log_param("fit_intercept", model.fit_intercept)
    
    # Mencatat metrik akurasi yang dihitung dari hasil prediksi
    mlflow.log_metric("accuracy", accuracy)
    
    # Menyimpan model yang sudah dilatih ke dalam MLflow
    # Infer the model signature
    signature = infer_signature(X_train, model.predict(X_train))
    
    # Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="iris_model",
        signature=signature,
        input_example=X_train,
        registered_model_name="tracking-quickstart",
    )
    
    # Menyimpan informasi tambahan jika diperlukan
    print(f"Model with accuracy: {accuracy} is saved!")

# Setelah eksperimen selesai, Anda dapat melihat log di UI MLflow
# Jalankan `mlflow ui` di terminal untuk melihat hasil pelacakan
