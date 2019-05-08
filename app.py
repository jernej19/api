from flask import Flask
from flask_restful import Api, Resource
import sqlite3

# Connect to database on my local drive
conn = sqlite3.connect('MarchMadness.db', check_same_thread=False)

app = Flask(__name__)
api = Api(app)


# API creation
class Standings(Resource):
    def get(self, name):
        query = conn.execute("SELECT * from standings_2016_final")
        keys1 = [a for a in query.fetchone()]
        for team in query.fetchall():
            if name in team[1]:
                return dict(zip(keys1, team)), 200


class Tournament(Resource):
    def get(self, name):
        query = conn.execute("SELECT * from tournament_2016_final")
        keys2 = [a for a in query.fetchone()]
        for team in query.fetchall():
            if name in team[1]:
                return dict(zip(keys2, team)), 200


api.add_resource(Standings, "/standings/<string:name>")
api.add_resource(Tournament, "/tournament/<string:name>")

app.run(debug=True)
