import json

with open('./data/games.json') as games_json:
    games = json.load(games_json)
    games_json.close()

newGames = []
for game in games:
    game['city'] = game['home_team']['city']

    game['homeTeamAbbr'] = game['home_team']['abbreviation']
    del game['home_team']

    game['awayTeamAbbr'] = game['visitor_team']['abbreviation']
    del game['visitor_team']

    newGames.append(game)


with open('./data/games.json', 'w') as games_json:
    json.dump(newGames, games_json)

    games_json.close()
