from config import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(200), unique=True, nullable=False)
    city = db.Column(db.String(200), unique=False, nullable=False)
    #website = db.Column(db.String(150), unique=True, nullable=False)
    
    # convert to json
    def to_dict(self):
        return {
            "id": self.id,
            "teamName": self.team_name,
            "city": self.city,
            # "website": self.website,
        }