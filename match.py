from flask_restful import Resource
from flask_restful import reqparse

import urllib
import json
from lxml import etree
import re

class Match(Resource):
    def get(self, match_id):
        details = dict()

        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
            str(match_id) + '.json')

        text = json.loads(match_json.read())

        print(match_id)

        details['id'] = match_id
        details['description'] = text['description']
        details['summary'] = text['match'].get('current_summary', None)

        details['batting'] = text['centre'].get('batting', None)
        if details['batting'] != None:
            for batting in details['batting']:
                batting.pop('preferred_shot', None)
                batting.pop('wagon_zone', None)    

        details['bowling'] = text['centre'].get('bowling', None)
        if details['bowling'] != None:
            for bowling in details['bowling']:
                bowling.pop('pitch_map_lhb', None)
                bowling.pop('pitch_map_rhb', None)
                bowling.pop('overall_lhb', None)
                bowling.pop('overall_rhb', None)

        details['officials'] = text['official']
        details['teams'] = text['team']
        details['series'] = text['series']
        details['match'] = text['match']
        details['innings'] = text['innings']     

        return details

class MatchId(Resource):
    def get(self):
        matches = etree.parse(
                "http://static.cricinfo.com/rss/livescores.xml").getroot()
        matches = matches.find('channel')
        matches = matches.findall('item')

        ids = list()

        for match in matches:
            link = match.find('guid').text
            match_id = re.search(r'(?:http:\/\/www.cricinfo.com\/ci\/engine\/match\/)([0-9]*)(?:.html)', link).group(1)

            ids.append(match_id)

        return ids