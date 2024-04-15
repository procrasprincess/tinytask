import React from "react"

const TeamList = ({teams}) => {

    return <div>
        <h2>Baseball Teams</h2>
        <table>
            <thead>
                <tr>
                    <th>Team Name</th>
                    <th>City</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {teams.map((team) => (
                    <tr key={team.id}>
                        <td>{team.teamName}</td>
                        <td>{team.city}</td>
                        <td>
                            <button>Update</button>
                            <button>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default TeamList