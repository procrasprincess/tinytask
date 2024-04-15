from flask import request, jsonify
from config import app, db
from models import Team

# crud

# GET: /teams
@app.route("/teams", methods=["GET"])

def get_teams():
    teams = Team.query.all() # get all python objects in Team
    json_teams = list(map(lambda x: x.to_json(), teams))
    
    return jsonify({"teams": json_teams}) # key-value: teams <> json_teams; convert to json


# POST: /create_team
@app.route("/create_team", methods=["POST"])

def create_team():
    team_name = request.json.get("teamName")
    city = request.json.get("city")
    #website = request.json.get("website")
    
    if not team_name or not city:
        return jsonify({"message": "You must include a team name and a city"}), 400
    
    new_team = Team(team_name=team_name, city=city)
    try:
        db.session.add(new_team) # add to db
        db.session.commit() # commit to db
    except Exception as e: # catch exception
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message":"Team Created!"}), 201


# PUT/PATCH: /update_team
@app.route("/update_team/<int:team_id>", methods=["PATCH"])

def update_team(team_id):
    team = Team.query.get(team_id)
    
    if not team:
        return jsonify({"message":"Team Not Found!"}), 404
    
    data = request.json
    # .get(): search for a key in dict; if exists, return that value, otherwise returns 2nd param value)
    team.team_name = data.get("teamName", team.team_name)
    team.city = data.get("city", team.city)
    
    db.session.commit()
    
    return jsonify({"message":"Team Not Found!"}), 200

# DELETE: /delete_team
@app.route("/delete_team/<int:team_id>", methods=["DELETE"])

def delete_team(team_id):
    team = Team.query.get(team_id)
    
    if not team:
        return jsonify({"message":"Team Not Found!"}), 404
    
    db.session.delete(team)
    db.session.commit()
    
    return jsonify({"message":"Team Deleted!"}), 200




# run this directly if it's not imported
if __name__ == '__main__':
    # create all if they don't already exist
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)