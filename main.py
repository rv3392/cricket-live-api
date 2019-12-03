from flask import Flask
from flask_restful import Resource, Api

from match import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Match, '/match/details/<int:match_id>/')
api.add_resource(MatchId, '/match/ids/')

if __name__ == '__main__':
    app.run(debug=True)

