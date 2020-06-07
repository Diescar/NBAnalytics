import json
from models import app, db, Player, Team, Game

def load_json(filename):
    with open(filename) as file:
        jason = json.load(file)
        file.close()

    return jason


def create_players():

    players = load_json('data/players.json')

    for player in players:

        newPlayer = Player(firstName = player['firstName'], lastName = player['lastName'], playerId = player['playerId'],
                            teamId = player['teamId'], height = player['height'], weight = player['weight'], age = player['age'], dob = player['dob'])

        db.session.add(newPlayer)
        db.session.commit()


def create_teams():

    teams = load_json('data/teams.json')

    for team in teams:

        newTeam = Team(teamId = team['teamId'], abbreviation = team['abbreviation'], teamName = team['teamName'], simpleName = team['simpleName'], location = team['location'],
                        stadium = team['stadium'], owner = team['owner'], headCoach = team['headCoach'], championships = team['championships'])

        db.session.add(newTeam)
        db.session.commit()

def create_games():

    games = load_json('data/games.json')

    for game in games:

        newGame = Game(gameId = game['id'], date = game['date'], season = game['season'], homeTeamAbbr = game['homeTeamAbbr'],
                        awayTeamAbbr = game['awayTeamAbbr'], homeTeamScore = game['home_team_score'], awayTeamScore = game['visitor_team_score'], postseason = game['postseason'], city = game['city'])

        db.session.add(newGame)
        db.session.commit()

create_teams()
create_players()
create_games()
