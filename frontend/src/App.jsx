import { useState, useEffect } from 'react'

function App() {
  const [stats, setStats] = useState(null)

  useEffect(() => {
    // Calling your FastAPI backend
    fetch('http://127.0.0.1:8000/stats/summary')
      .then(res => res.json())
      .then(data => setStats(data))
      .catch(err => console.error("Backend not running:", err))
  }, [])

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center p-10 font-sans">
      <header className="mb-12 text-center">
        <h1 className="text-4xl font-bold text-black tracking-tight">AI Resource Tracker</h1>
        <p className="text-gray-500 mt-2">Real-time environmental impact of local LLM usage.</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-5xl">
        {/* Water Usage Card */}
        <div className="bg-white p-6 border-l-4 border-blue-500 shadow-sm">
          <h2 className="text-sm uppercase font-semibold text-gray-400">Water Consumed</h2>
          <p className="text-3xl font-bold text-black">{stats ? stats.metrics.water_liters : "..."} L</p>
        </div>

        {/* Carbon Usage Card */}
        <div className="bg-white p-6 border-l-4 border-gray-800 shadow-sm">
          <h2 className="text-sm uppercase font-semibold text-gray-400">Carbon Footprint</h2>
          <p className="text-3xl font-bold text-black">{stats ? stats.metrics.carbon_grams : "..."} g</p>
        </div>

        {/* Total Events Card */}
        <div className="bg-white p-6 border-l-4 border-green-500 shadow-sm">
          <h2 className="text-sm uppercase font-semibold text-gray-400">Total Queries</h2>
          <p className="text-3xl font-bold text-black">{stats ? stats.total_usage_events : "..."}</p>
        </div>
      </div>
    </div>
  )
}

export default App