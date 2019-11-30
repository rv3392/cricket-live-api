from flask_restful import Resource
from flask_restful import reqparse

import urllib
import json
from lxml import etree
import re

class MatchIds(Resource):
    def get(self):
        matches = etree.parse(
                "http://static.cricinfo.com/rss/livescores.xml").getroot()
        matches = matches.find('channel')
        matches = matches.findall('item')

        match_ids = dict()

        for match in matches:
            link = match.find('guid').text
            description = match.find('description').text

            match_id = re.search(r'(?:http:\/\/www.cricinfo.com\/ci\/engine\/match\/)([0-9]*)(?:.html)', link).group(1)
            match_ids[match_id] = description
        
        print(match_ids)
        return match_ids

class Match(Resource):
    def get(self, match_id):
        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
                str(match_id) + '.json')

        text = json.loads(match_json.read())

        return text

            
        
        
        