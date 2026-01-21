import numpy as np
import torch
import torch.nn as nn
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler

from NST import NonStationaryTransformer

# Load data
ticker = "AAPL"
data = yf.download(ticker, start="2020-01-01", end="2024-01-01")

prices = data["Close"].values.reshape(-1, 1)

scaler = MinMaxScaler()
scaled = scaler.fit_transform(prices)

# Create sequences
SEQ_LEN = 30

X, y = [], []

for i in range(len(scaled) - SEQ_LEN):
    X.append(scaled[i:i+SEQ_LEN])
    y.append(scaled[i+SEQ_LEN])

X = torch.tensor(np.array(X), dtype=torch.float32)
y = torch.tensor(np.array(y), dtype=torch.float32)

# Model
model = NonStationaryTransformer()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training
EPOCHS = 5   

for epoch in range(EPOCHS):
    optimizer.zero_grad()
    output = model(X)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()

    print(f"Epoch {epoch+1}/{EPOCHS} | Loss: {loss.item():.6f}")

# Save model
torch.save(model.state_dict(), "model.pth")

print("✅ Model trained and saved as model.pth")
