from flask import Flask
from flask_restful import Resource, Api

from match import *

app = Flask(__name__)
api = Api(app)

api.add_resource(MatchIds, '/match/ids')
api.add_resource(Match, '/match/all/<int:match_id>')
api.add_resource(MatchRecent, '/match/recent/<int:match_id>')
api.add_resource(Innings, '/match/innings/<int:match_id>')
api.add_resource(Description, '/match/description/<int:match_id>')
api.add_resource(Summary, '/match/summary/<int:match_id>')
api.add_resource(Status, '/match/status/<int:match_id>')
api.add_resource(CurrentBatsmen, '/match/current_batsmen/<int:match_id>')
api.add_resource(CurrentBowlers, '/match/current_bowlers/<int:match_id>')
api.add_resource(TeamDetails, '/match/team_details/<int:match_id>')
api.add_resource(TeamNames, '/match/team_names/<int:match_id>')
api.add_resource(TeamLogos, '/match/team_logos/<int:match_id>')

if __name__ == '__main__':
    app.run(debug=True)

