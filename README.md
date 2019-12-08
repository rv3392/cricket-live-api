<h2>Cricket Live API</h2>
<b>The cricket live REST API provides a simple way to retrieve details about current cricket matches.</b>

Note: This was made for my personal use in various projects and everything may not work as intended.

Features are currently implemented:
- Getting all details about a particular match in JSON format

<h4><b>Endpoints:</b></h4>

<b>GET - https://cricket-live-api.herokuapp.com/match/ids/</b>

Retrieves the espncricinfo.com Ids of all matches currently being played in the format: [id-1, id-2, id-3, ... id-n].

<b>GET - https://cricket-live-api.herokuapp.com/match/details/[id]</b>

Retrieves the details of the match with the provided id.
e.g. https://cricket-live-api.herokuapp.com/match/details/1199422 would return the details of match "1199422" in JSON format.

<h4>How to Use:</h4>

1. Retrieve the ids using https://cricket-live-api.herokuapp.com/match/ids/
2. Retrieve the details for the match using an id from this list (https://cricket-live-api.herokuapp.com/match/details/[id])




