from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING", "postgres://postgres:asd123@localhost:5432/nba")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(64), nullable = False)
    lastName = db.Column(db.String(64), nullable = False)
    playerId = db.Column(db.BIGINT, nullable = False) #pket
    teamId = db.Column(db.BIGINT, nullable = False)
    height = db.Column(db.String(64))
    weight = db.Column(db.String(64))
    age = db.Column(db.String(32))
    dob = db.Column(db.String(32))

    def serialize(self):
        return {
            'firstName' : self.firstName,
            'lastName' : self.lastName,
            'playerId' : self.playerId,
            'teamId' : self.teamId,
            'height' : self.height,
            'weight' : self.weight,
            'age' : self.age,
            'dob' : self.dob
        }


class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teamId = db.Column(db.BIGINT, nullable = False) #pkey
    abbreviation = db.Column(db.String(64), nullable = False)
    teamName = db.Column(db.String(64), nullable = False)
    simpleName = db.Column(db.String(64), nullable = False)
    location = db.Column(db.String(64), nullable = False)
    stadium = db.Column(db.String(64), nullable = False)
    owner = db.Column(db.String(64), nullable = False)
    headCoach = db.Column(db.String(64), nullable = False)
    championships = db.Column(db.ARRAY(db.Integer), nullable = False)

    def serialize(self):
        return {
            'teamId' : self.teamId,
            'abbreviation' : self.abbreviation,
            'teamName' : self.teamName,
            'simpleName' : self.simpleName,
            'location' : self.location,
            'stadium' : self.stadium,
            'owner' : self.owner,
            'headCoach' : self.headCoach,
            'championships' : self.championships
        }

class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gameId = db.Column(db.BIGINT, nullable = False) #pkey
    date = db.Column(db.String(64), nullable = False)
    season = db.Column(db.BIGINT, nullable = False)
    homeTeamAbbr = db.Column(db.String(64), nullable = False)
    awayTeamAbbr = db.Column(db.String(64), nullable = False)
    homeTeamScore = db.Column(db.BIGINT, nullable = False)
    awayTeamScore = db.Column(db.BIGINT, nullable = False)
    postseason = db.Column(db.Boolean, nullable = False)
    city = db.Column(db.String(64), nullable = False)

    def serialize(self):
        return {
            'gameId' : self.gameId,
            'date' : self.date,
            'season' : self.season,
            'homeTeamAbbr' : self.homeTeamAbbr,
            'awayTeamAbbr' : self.awayTeamAbbr,
            'homeTeamScore' : self.homeTeamScore,
            'awayTeamScore' : self.awayTeamScore,
            'postseason' : self.postseason,
            'city' : self.city
        }

db.drop_all()
db.create_all()
