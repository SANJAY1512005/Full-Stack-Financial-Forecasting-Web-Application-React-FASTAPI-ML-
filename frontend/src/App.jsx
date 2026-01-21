import { useState } from "react";
import axios from "axios";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend
} from "recharts";

function App() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  const predictStock = async () => {
    setLoading(true);

    const res = await axios.post(
      "http://127.0.0.1:8000/predict?ticker=AAPL&days=30"
    );

    const historical = res.data.historical.map((v, i) => ({
      day: i,
      price: v
    }));

    const predicted = res.data.predicted.map((v, i) => ({
      day: historical.length + i,
      predicted: v
    }));

    const merged = [...historical, ...predicted];
    setData(merged);

    setLoading(false);
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>📈 Stock Prediction App</h1>

      <button onClick={predictStock}>
        Predict AAPL
      </button>

      {loading && <p>Loading...</p>}

      {data.length > 0 && (
        <LineChart width={900} height={400} data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="day" />
          <YAxis />
          <Tooltip />
          <Legend />

          <Line
            type="monotone"
            dataKey="price"
            stroke="#4f46e5"
            dot={false}
            name="Historical"
          />

          <Line
            type="monotone"
            dataKey="predicted"
            stroke="#ef4444"
            dot={false}
            strokeDasharray="5 5"
            name="Predicted"
          />
        </LineChart>
      )}
    </div>
  );
}

export default App;
