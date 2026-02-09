export default function RiskPanel({ risk }){

  const color = risk?.level==="Severe"?"bg-red-600":
                risk?.level==="Moderate"?"bg-orange-500":"bg-green-600"

  return (
    <div className={`p-5 rounded-xl text-white ${color}`}>
      <h2 className="text-xl font-bold"> Risk Intelligence</h2>

      <p className="mt-2">Severity: {risk?.level}</p>
      <p>Impact: {risk?.impact}</p>
      <p>Recommended Action: {risk?.action}</p>
    </div>
  )
}
