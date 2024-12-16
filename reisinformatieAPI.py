from private import *
from tryto import trytostring
import datetime
import urllib.request
import json

class reisinformatie():
    def __init__(self, lang, uicCode, maxJourneys):
        self.lang = lang
        self.uicCode = uicCode
        self.dateTime = trytostring(datetime.datetime.now(datetime.timezone.utc).isoformat())
        self.maxJourneys = maxJourneys
        self.url = "https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/arrivals?lang=" + self.lang + "&uicCode=" + self.uicCode + "&dateTime=" + self.dateTime + "&maxJourneys=" + self.maxJourneys + ""
        self.hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
        'Ocp-Apim-Subscription-Key': nsapi_key
        }

    def get_reis_informatie(self):
        req = urllib.request.Request(self.url, headers=self.hdr)

        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)
        Response_String = trytostring(response.read()).strip("'b")

        with open("response.json", "w", encoding="utf-8") as file:
            file.write(Response_String)

        # Read the JSON data from the file
        with open("response.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # Write the JSON data back to the file with indentation for better readability
        with open("response.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        with open("response.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # Example: Accessing specific values from the JSON data
        arrivals = data.get("payload", {}).get("arrivals", [])
        results = []

        for arrival in arrivals:
            result = [
                arrival.get("origin"),
                arrival.get("actualDateTime"),
                arrival.get("actualTrack"),
            ]
            results.append(result)

        return results