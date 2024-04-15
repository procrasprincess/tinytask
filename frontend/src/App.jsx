import { useState, useEffect } from 'react'
import TeamList from './TeamsList'
import './App.css'


function App() {
  const [teams, setTeams] = useState([{"teamName": "Arizona Diamondbacks", "city": "Phenoix", id: 1 }])

  useEffect(() => {
    //fetchTeams()
  }, [])

  const fetchTeams = async () => {
    const response = await fetch("http://127.0.0.1:5000/teams")
    const data = await response.json()
    setTeams(data.teams)
    console.log(data.teams)

  }

  return <TeamList teams={teams}/>
}

export default App
