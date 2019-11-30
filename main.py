from flask import Flask
from flask_restful import Resource, Api

from match import MatchIds
from match import Match

app = Flask(__name__)
api = Api(app)

api.add_resource(MatchIds, '/matches')
api.add_resource(Match, '/match/<int:match_id>')

if __name__ == '__main__':
    app.run(debug=True)

