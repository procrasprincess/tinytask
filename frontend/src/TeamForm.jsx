import React from "react"

const TeamForm = ({ }) => {
    //states for db vars
    const [teamName, setTeamName] = useState("");
    const [city, setCity] = useState("");
    
    // action: submit
    const onSubmit = (e) => {
        e.preventDefault()

        const data = {
            teamName,
            city
        }

        const url = "http://127.0.0.1:5000/create_team"

        const options = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        
        const response = await fetch(url, options)
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            updateCallback()
        }
    }

    return (
        <form>
            <div>
                <label htmlFor="teamName">Team Name:</label>
                <input 
                    type="text"
                    id="teamName"
                    value={teamName}
                    onChange={(e) => setTeamName(e.target.value)}
                />    
            </div>

            <div>
                <label htmlFor="city">City:</label>
                <input 
                    type="text"
                    id="city"
                    value={city}
                    onChange={(e) => setCity(e.target.value)}
                />    
            </div>
            <button type="submit">Create Team</button>
        </form>
    );
};   

export default TeamForm