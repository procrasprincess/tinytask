import { useState, useEffect } from 'react';
import TeamList from './TeamList';
import './App.css';
import TeamForm from './TeamForm';


function App() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetchTeams()
  }, []);
  
  const fetchTeams = async() => {
    const response = await fetch("http://127.0.0.1:5000/teams");
    const data = await response.json();
    setTeams(data.teams);
    console.log(data.teams);
  };

  return (
    <>
      <TeamList teams={teams} />
      <TeamForm />
    </>
  );
}

export default App
