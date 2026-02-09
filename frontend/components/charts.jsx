import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function Charts({ data }){

  return (
    <div className="bg-slate-800 p-4 rounded-xl">
      <h2 className="text-lg font-semibold mb-2">Climate Trends</h2>

      <ResponsiveContainer width="100%" height={250}>
        <LineChart data={data}>
          <XAxis dataKey="year"/>
          <YAxis/>
          <Tooltip/>
          <Line type="monotone" dataKey="temperature" strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>

    </div>
  )
}
