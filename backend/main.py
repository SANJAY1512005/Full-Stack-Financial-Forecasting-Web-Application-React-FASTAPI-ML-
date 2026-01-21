from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import torch
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from NST import NonStationaryTransformer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = NonStationaryTransformer()
model.load_state_dict(torch.load("model.pth", map_location="cpu"))
model.eval()


@app.get("/")
def root():
    return {"status": "API running"}


@app.post("/predict")
def predict(ticker: str = "AAPL", days: int = 30):
    data = yf.download(ticker, period="2y")

    prices = data["Close"].values.reshape(-1, 1)

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(prices)

    seq_len = 30
    seq = scaled[-seq_len:].reshape(1, seq_len, 1)

    future = []

    with torch.no_grad():
        for _ in range(days):
            inp = torch.tensor(seq, dtype=torch.float32)
            pred = model(inp).item()
            future.append(pred)

            new_seq = np.append(seq[0, 1:, 0], pred)
            seq = new_seq.reshape(1, seq_len, 1)

    future = scaler.inverse_transform(
        np.array(future).reshape(-1, 1)
    ).flatten()

    return {
        "ticker": ticker,
        "historical": prices.flatten().tolist(),
        "predicted": future.tolist()
    }
