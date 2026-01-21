📈 Full-Stack Financial Forecasting Web Application

React • FastAPI • Machine Learning (PyTorch)

A complete full-stack financial forecasting system that predicts future stock prices using a deep learning time-series model and provides interactive visualization through a modern web interface.

🚀 Project Overview

This application allows users to:

Enter a stock ticker (e.g., AAPL)

Fetch real historical stock data

Use a trained Non-Stationary Transformer model

Predict future stock prices

Visualize historical vs predicted prices on an interactive chart

The project demonstrates end-to-end ML integration into a full-stack web application — from model training to real-time inference via API.

🧠 Key Features

📊 Real stock market data using Yahoo Finance

🤖 Machine Learning time-series forecasting

⚡ FastAPI backend for high-performance inference

🌐 React frontend with interactive charts

📈 Visualization using Recharts

🔁 Separation of training and prediction pipelines

💾 Pre-trained model loading for fast predictions

🏗️ Project Architecture
stock-prediction-app/
│
├── backend/
│   ├── main.py              # FastAPI server
│   ├── train.py             # ML model training
│   ├── NST.py               # Transformer model
│   ├── model.pth            # Trained model weights
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx          # React UI
│   │   └── index.css
│   └── package.json
│
└── README.md

🧠 Machine Learning Details

Model: Non-Stationary Transformer (PyTorch)

Input: Historical stock closing prices

Sequence Length: 30 days

Output: Future price prediction

Loss Function: Mean Squared Error (MSE)

Optimizer: Adam

Framework: PyTorch

The model is trained once using train.py and saved as:

model.pth


During prediction:

❌ No retraining

✅ Only forward pass

⚡ Very fast inference

🔧 Tech Stack
Frontend

React (Vite)

JavaScript

Axios

Recharts

CSS

Backend

FastAPI

Python

Uvicorn

Machine Learning

PyTorch

NumPy

Scikit-learn

Yahoo Finance API

Tools

Git & GitHub

VS Code

REST APIs

▶️ How It Works

User clicks Predict

React sends request to FastAPI backend

Backend:

Loads trained model.pth

Fetches historical stock data

Scales data

Performs forward prediction

Backend returns:

Historical prices

Predicted future prices

Frontend visualizes data in a chart

⚙️ Setup Instructions
Backend
cd backend
pip install -r requirements.txt
python train.py
python -m uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000

Frontend
cd frontend
npm install
npm run dev


Frontend runs at:

http://localhost:5173

📊 Sample Output

Blue line → Historical prices

Red dotted line → Predicted prices

The application displays both in a single interactive chart.

📌 Why This Project is Important

This project demonstrates:

Real-world ML deployment

Full-stack architecture

Model inference optimization

API communication

Clean separation of training vs prediction

Production-style workflow

It closely resembles industry ML web applications.

🧑‍💻 Author

Sanjay S
Full-Stack Developer | Machine Learning Enthusiast

GitHub:
https://github.com/SANJAY1512005

⭐ Future Improvements

User authentication

Multiple stock comparison

LSTM vs Transformer comparison

Model performance metrics

Cloud deployment (AWS / Render)

Live market updates

📜 Disclaimer

This project is for educational purposes only and should not be used for real financial trading decisions.
