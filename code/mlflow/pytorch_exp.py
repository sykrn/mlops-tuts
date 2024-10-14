import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
import mlflow
import mlflow.pytorch

# Definisikan model neural network sederhana
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.layer1 = nn.Linear(28*28, 128)
        self.layer2 = nn.Linear(128, 10)
    
    def forward(self, x):
        x = x.view(-1, 28*28)  # Flatten the input
        x = torch.relu(self.layer1(x))
        x = self.layer2(x)
        return x

# Definisikan fungsi pelatihan
def train(model, device, train_loader, optimizer, epoch):
    model.train()
    loss_fn = nn.CrossEntropyLoss()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = loss_fn(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            print(f'Epoch {epoch}, Batch {batch_idx}, Loss: {loss.item():.6f}')
    return loss.item()

# Fungsi evaluasi akurasi
def test(model, device, test_loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            _, predicted = torch.max(output.data, 1)
            total += target.size(0)
            correct += (predicted == target).sum().item()
    accuracy = correct / total
    print(f'Test Accuracy: {accuracy:.4f}')
    return accuracy

# Set device untuk GPU jika tersedia
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load dataset MNIST
transform = transforms.Compose([transforms.ToTensor()])
train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST('./data', train=False, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=1000, shuffle=False)

# Model, optimizer, dan hyperparameter
model = SimpleNN().to(device)
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Mulai eksperimen dengan MLflow
mlflow.set_experiment("PyTorch_Experiment_MNIST")

# Logging dengan MLflow
with mlflow.start_run():
    mlflow.log_param("optimizer", "Adam")
    mlflow.log_param("learning_rate", 0.001)
    mlflow.log_param("batch_size", 64)
    
    epochs = 5
    for epoch in range(1, epochs + 1):
        train_loss = train(model, device, train_loader, optimizer, epoch)
        accuracy = test(model, device, test_loader)

        # Log metrik di setiap epoch
        mlflow.log_metric("train_loss", train_loss, step=epoch)
        mlflow.log_metric("accuracy", accuracy, step=epoch)
    
    # Log model menggunakan MLflow PyTorch
    mlflow.pytorch.log_model(model, "model")

    print("Model dan hasil eksperimen telah tercatat di MLflow.")
