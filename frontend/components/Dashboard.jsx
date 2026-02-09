import { LineChart,Line,XAxis,YAxis,Tooltip,ResponsiveContainer } from 'recharts';
import axios from 'axios';
import { useState } from 'react';

export default function Dashboard(){

  const [data,setData] = useState(null);

  const predict = async ()=>{
    const res = await axios.get("http://localhost:8000/predict?year=2025&month=7&t12=25&t24=24&anomaly=1.6");
    setData(res.data);
  }

  return(
    <div className="p-6 bg-slate-900 min-h-screen text-white">
      <h1 className="text-3xl font-bold">🌍 Climate Risk Intelligence</h1>

      <button onClick={predict} className="mt-4 px-6 py-2 bg-green-600 rounded">
        Run Prediction
      </button>

      {data && (
        <div className="mt-6 p-4 bg-slate-800 rounded-xl">
          <p>Risk Level: {data.risk.level}</p>
          <p>Action: {data.risk.action}</p>
          <p>Impact: {data.risk.impact}</p>
        </div>
      )}
    </div>
  )
}
