import os
import sys
import unittest
from flask import Flask, render_template
from models import db, Player, Team, Game
from create_db import create_teams, create_players, create_games

def create_app(cfg=None):
    app = Flask(__name__)
    return app


class TestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('test_app')
        cls.client = cls.app.test_client()

        @cls.app.route('/')
        def index():
            return render_template('index.html')

        @cls.app.route('/teams/')
        def teams():
            return render_template('teams.html')

        @cls.app.route('/games/')
        def games():
            return render_template('games.html')

        @cls.app.route('/about/')
        def about():
            return render_template('about.html')

        @cls.app.route('/search/')
        def search():
            return render_template('search.html')
            
    # write unit tests here, e.g. def test_source_insert_1(self):

    def test_index_template_rendered_1(self):
        response = self.client.get('/')
        self.assertTrue('data-address-tag="index"' in response.get_data(as_text=True))

    def test_teams_template_rendered_1(self):
        response = self.client.get('/teams/')
        self.assertTrue('data-address-tag="teams"' in response.get_data(as_text=True))

    def test_games_template_rendered_1(self):
        response = self.client.get('/games/')
        self.assertTrue('data-address-tag="games"' in response.get_data(as_text=True))

    def test_about_template_rendered_1(self):
        response = self.client.get('/about/')
        self.assertTrue('data-address-tag="about"' in response.get_data(as_text=True))
    
    #-----------------------------------
    #Database Adding and Removing Player
    #-----------------------------------
        
    def test_DB_create_players_01(self):
        newPlayer = Player(firstName = "Michael", lastName = "Jordan", playerId = 1, 
                            teamId = 1610612741, height = "6-6", weight = "216 lbs", 
                            age = "57", dob = "02/17/1963")
        db.session.add(newPlayer)
        db.session.commit()
        
        query1 = Player.query.filter_by(playerId = 1).first()
        self.assertEqual(newPlayer, query1)
        
        db.session.delete(newPlayer)
        db.session.commit()
        
        query2 = Player.query.filter_by(playerId = 1).first()
        self.assertNotEqual(newPlayer, query2)
        
    def test_DB_create_players_02(self):
        newPlayer = Player(firstName = "34232523", lastName = "00000", playerId = 999999, 
                            teamId = 1610612741, height = "7-11", weight = "999 lbs", 
                            age = "99", dob = "01/01/1000")
        db.session.add(newPlayer)
        db.session.commit()
        
        query1 = Player.query.filter_by(playerId = 999999).first()
        self.assertEqual(newPlayer, query1)
        
        db.session.delete(newPlayer)
        db.session.commit()
        
        query2 = Player.query.filter_by(playerId = 999999).first()
        self.assertNotEqual(newPlayer, query2)

    def test_DB_create_players_03(self):
        newPlayer = Player(firstName = "A", lastName = "B", playerId = 50, 
                            teamId = 1610612741, height = "8", weight = "1 lbs", 
                            age = "1", dob = "99/99/9999")
        db.session.add(newPlayer)
        db.session.commit()
        
        query1 = Player.query.filter_by(playerId = 50).first()
        self.assertEqual(newPlayer, query1)
        
        db.session.delete(newPlayer)
        db.session.commit()
        
        query2 = Player.query.filter_by(playerId = 50).first()
        self.assertNotEqual(newPlayer, query2)

    #----------------------------------
    #Database Adding and Removing Team
    #----------------------------------
    
    def test_DB_create_teams_01(self):
        newTeam = Team(teamId = 1111, abbreviation = "ATX", teamName = "UT Longhorns", simpleName = "Longhorns", location = "Austin",
                        stadium = "Frank Erwin Center", owner = "Chris Del Conte", headCoach = "Shaka Smart", championships = [])
        db.session.add(newTeam)
        db.session.commit()
        
        query1 = Team.query.filter_by(teamId = 1111).first()
        self.assertEqual(newTeam, query1)
        
        db.session.delete(newTeam)
        db.session.commit()
        
        query2 = Team.query.filter_by(teamId = 1111).first()
        self.assertNotEqual(newTeam, query2)
        
    def test_DB_create_teams_02(self):
        newTeam = Team(teamId = 0, abbreviation = "", teamName = "", simpleName = "", location = "",
                        stadium = "", owner = "", headCoach = "", championships = [])
        db.session.add(newTeam)
        db.session.commit()
        
        query1 = Team.query.filter_by(teamId = 0).first()
        self.assertEqual(newTeam, query1)
        
        db.session.delete(newTeam)
        db.session.commit()
        
        query2 = Team.query.filter_by(teamId = 0).first()
        self.assertNotEqual(newTeam, query2)

    def test_DB_create_teams_03(self):
        newTeam = Team(teamId = 50, abbreviation = "CB", teamName = "Chicago Bulls", simpleName = "Bulls", location = "Chicago",
                        stadium = "Soldier Field", owner = "Jerry", headCoach = "Jim", championships = [])
        db.session.add(newTeam)
        db.session.commit()
        
        query1 = Team.query.filter_by(teamId = 50).first()
        self.assertEqual(newTeam, query1)
        
        db.session.delete(newTeam)
        db.session.commit()
        
        query2 = Team.query.filter_by(teamId = 0).first()
        self.assertNotEqual(newTeam, query2)
        
    #----------------------------------
    #Database Adding and Removing Game
    #----------------------------------
        
    def test_DB_create_games_01(self):
        newGame = Game(gameId = 101, date = "2019-01-01T00:00:00.000Z", season = 2019, homeTeamAbbr = "BOS",
                        awayTeamAbbr = "ATL", homeTeamScore = 100, awayTeamScore = 1, postseason = False, city = "Boston")

        db.session.add(newGame)
        db.session.commit()
        
        query1 = Game.query.filter_by(gameId = 101).first()
        self.assertEqual(newGame, query1)
        
        db.session.delete(newGame)
        db.session.commit()
        
        query2 = Game.query.filter_by(gameId = 101).first()
        self.assertNotEqual(newGame, query2)
        
    def test_DB_create_games_02(self):
        newGame = Game(gameId = 10101, date = "2000-01-01T00:00:00.000Z", season = 1, homeTeamAbbr = "",
                        awayTeamAbbr = "", homeTeamScore = 12, awayTeamScore = 15, postseason = False, city = "")

        db.session.add(newGame)
        db.session.commit()
        
        query1 = Game.query.filter_by(gameId = 10101).first()
        self.assertEqual(newGame, query1)
        
        db.session.delete(newGame)
        db.session.commit()
        
        query2 = Game.query.filter_by(gameId = 10101).first()
        self.assertNotEqual(newGame, query2)

    def test_DB_create_games_03(self):
        newGame = Game(gameId = 1, date = "1900-10-05T12:34:45.000Z", season = 99, homeTeamAbbr = "ABC",
                        awayTeamAbbr = "CBA", homeTeamScore = 1, awayTeamScore = 0, postseason = True, city = "Austin")

        db.session.add(newGame)
        db.session.commit()
        
        query1 = Game.query.filter_by(gameId = 1).first()
        self.assertEqual(newGame, query1)
        
        db.session.delete(newGame)
        db.session.commit()
        
        query2 = Game.query.filter_by(gameId = 1).first()
        self.assertNotEqual(newGame, query2)
              
if __name__ == '__main__':
    unittest.main()
