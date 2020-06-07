from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
import json, requests
import subprocess
from create_db import app, db, Player, Team, Game
from sqlalchemy import or_, and_, func

# note to self(Mills): run with $ python3 main.py

@app.route('/')
def index():
    return render_template('splash.html')

@app.route('/teams/')
def all_teams_page():
    teams = db.session.query(Team).all()
    return render_template('teams.html', teams = teams)

@app.route('/teams/<abbr>')
def single_team_page(abbr):

    team = db.session.query(Team).filter(Team.abbreviation == abbr).first()

    teamPlayers = db.session.query(Player).filter(Player.teamId == team.teamId)

    games = db.session.query(Game).filter(or_(Game.homeTeamAbbr == team.abbreviation, Game.awayTeamAbbr == team.abbreviation)).all()

    return render_template('team.html', team = team, players = teamPlayers, games = games)

@app.route('/players/<page_num>')
def all_players_page(page_num):

    players = db.session.query(Player).all()

    page_num = int(page_num)

    page_range = [1,2,3,4,5,6,7,8,9,10,11]

    subPlayers = players[(page_num - 1) * 48: page_num * 48]

    return render_template('players.html', players = subPlayers, page_range = page_range, page_num = page_num)

@app.route('/player/<playerId>')
def single_player_page(playerId):

    player = None
    playerId = int(playerId)

    player = db.session.query(Player).filter(Player.playerId == playerId).first()

    team = db.session.query(Team).filter(Team.teamId == player.teamId).first()

    teamPlayers = db.session.query(Player).filter(and_(Player.teamId == team.teamId, Player.playerId != playerId)).all()

    recentGames = db.session.query(Game).filter(or_(Game.homeTeamAbbr == team.abbreviation, Game.awayTeamAbbr == team.abbreviation))

    if not player:
        return "No player found"

    return render_template('player.html', player = player, team = team, teamPlayers = teamPlayers, games = recentGames)


def get_gitlab():
    parameters = {'private token': 'vqspJG_XdJdaJzsKuGEb'}
    project_id = str(16870416)
    url = 'https://gitlab.com/api/v4/projects/'+project_id+'/repository/commits'
    response = requests.get(url,params=parameters)
    print(response.status_code)
    content = response.json()
    for c in content:
        print(c, '\n')
    return content

@app.route('/about/', methods=['GET', 'POST'])
def about():
    content = get_gitlab()
    message = ""
    if request.method == "POST":
        message = subprocess.getoutput("python test.py")
    return render_template('about.html', message=message)

@app.route('/games/')
def all_games_page():
    games = db.session.query(Game).all()

    return render_template('games.html', games = games)

@app.route('/search/', methods=["POST", "GET"])
def search():
    if request.method == 'POST':
        term = request.form["term"]
    else: 
        term = ""
        
    players = db.session.query(Player).filter(or_(func.lower(Player.firstName).contains(func.lower(term)), func.lower(Player.lastName).contains(func.lower(term)))).all()

    teams = db.session.query(Team).filter(or_(func.lower(Team.teamName).contains(func.lower(term)), func.lower(Team.stadium).contains(func.lower(term)), func.lower(Team.owner).contains(func.lower(term)), func.lower(Team.headCoach).contains(func.lower(term)))).all()

    games = db.session.query(Game).filter(or_(func.lower(Game.homeTeamAbbr).contains(func.lower(term)), func.lower(Game.awayTeamAbbr).contains(func.lower(term)), func.lower(Game.city).contains(func.lower(term)))).all()

    return render_template('search.html', players=players, teams=teams, games=games)

@app.route('/teams/JSON')
def JSON_teams():
    with open('data/teams.json') as f:
        data = json.load(f)
    r = json.dumps(data)
    return Response(r)

@app.route('/players/JSON')
def JSON_players():
    with open('data/players.json') as f:
        data = json.load(f)
    r = json.dumps(data)
    return Response(r)

@app.route('/games/JSON')
def JSON_games():
    with open('data/games.json') as f:
        data = json.load(f)
    r = json.dumps(data)
    return Response(r)

if __name__ == "__main__":
    app.run(debug = True)
