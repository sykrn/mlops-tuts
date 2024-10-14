import mlflow
import mlflow.tensorflow
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Load dataset MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocessing dataset
train_images = train_images.reshape((60000, 28, 28, 1)).astype("float32") / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype("float32") / 255

# Set parameters
batch_size = 64
learning_rate = 0.001
epochs = 5

# Buat model neural network
def create_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    return model

# Mulai eksperimen dengan MLflow
mlflow.set_experiment("TensorFlow_Experiment_MNIST")

with mlflow.start_run():
    # Logging parameters
    mlflow.log_param("batch_size", batch_size)
    mlflow.log_param("learning_rate", learning_rate)
    
    # Buat dan kompilasi model
    model = create_model()
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    # Melatih model dan mencatat setiap epoch
    history = model.fit(train_images, train_labels, 
                        epochs=epochs, 
                        batch_size=batch_size, 
                        validation_data=(test_images, test_labels))
    
    # Log metrics untuk setiap epoch
    for epoch in range(epochs):
        mlflow.log_metric("loss", history.history['loss'][epoch], step=epoch + 1)
        mlflow.log_metric("accuracy", history.history['accuracy'][epoch], step=epoch + 1)
        mlflow.log_metric("val_loss", history.history['val_loss'][epoch], step=epoch + 1)
        mlflow.log_metric("val_accuracy", history.history['val_accuracy'][epoch], step=epoch + 1)
    
    # Log model menggunakan MLflow TensorFlow
    mlflow.tensorflow.log_model(model, "model")

    print("Model dan hasil eksperimen telah tercatat di MLflow.")
