import { MapContainer, TileLayer, CircleMarker, Popup } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'

const points = [
  { city: "Delhi", lat:28.61, lng:77.23, risk:0.92 },
  { city: "Mumbai", lat:19.07, lng:72.87, risk:0.84 },
  { city: "Chennai", lat:13.08, lng:80.27, risk:0.79 },
  { city: "Kolkata", lat:22.57, lng:88.36, risk:0.88 }
]

export default function Map(){

  return(
    <div className="bg-slate-800 p-4 rounded-xl h-[400px]">
      <h2 className="text-lg font-semibold mb-2"> Disaster Risk Map</h2>

      <MapContainer center={[22,78]} zoom={5} className="h-[350px] rounded-lg">
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/>

        {points.map((p,i)=>(
          <CircleMarker
            key={i}
            center={[p.lat,p.lng]}
            radius={15*p.risk}
            color={p.risk>0.85?"red":"orange"}
          >
            <Popup>
              <b>{p.city}</b><br/>
              Risk Level: {(p.risk*100).toFixed(1)}%
            </Popup>
          </CircleMarker>
        ))}

      </MapContainer>
    </div>
  )
}
