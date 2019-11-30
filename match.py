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

class MatchRecent(Resource):
    def get(self, match_id):
        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
                str(match_id) + '.json')

        text = json.loads(match_json.read())
        return text["live"]

class Status(Resource):
    def get(self, match_id):
        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
                str(match_id) + '.json')

        text = json.loads(match_json.read())
        return text["live"]["status"]

class Innings(Resource):
    def get(self, match_id):
        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
                str(match_id) + '.json')
        
        text = json.loads(match_json.read())
        return text["innings"]
            
class Description(Resource):
    def get(self, match_id):
        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
                str(match_id) + '.json')
        
        text = json.loads(match_json.read())
        return text["description"]

class Summary(Resource):
    def get(self, match_id):
        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
                str(match_id) + '.json')
        
        text = json.loads(match_json.read())
        return text["match"]["current_summary"]

class Break(Resource):
    def get(self, match_id):
        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
                str(match_id) + '.json')
        
        text = json.loads(match_json.read())
        return text["match"]["current_summary"]
        
class CurrentBatsmen(Resource):
    def get(self, match_id):
        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
                str(match_id) + '.json')
        
        text = json.loads(match_json.read())
        return text["centre"]["batting"]

class CurrentBowlers(Resource):
    def get(self, match_id):
        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
                str(match_id) + '.json')
        
        text = json.loads(match_json.read())
        return text["centre"]["bowling"]

class TeamDetails(Resource):
    def get(self, match_id):
        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
                str(match_id) + '.json')
        
        text = json.loads(match_json.read())
        return text["team"]

class TeamNames(Resource):
    def get(self, match_id):
        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
                str(match_id) + '.json')
        
        text = json.loads(match_json.read())
        teams = text["team"]
        
        names = list()
        for team in teams:
            names.append(team["team_name"])

        return names

class TeamLogos(Resource):
    def get(self, match_id):
        match_json = urllib.request.urlopen('http://www.cricinfo.com/ci/engine/match/' + 
                str(match_id) + '.json')
        
        text = json.loads(match_json.read())
        teams = text["team"]
        
        logos = dict()
        for team in teams:
            logos[team["team_name"]] = team["logo_image_path"]

        return logos

        
        