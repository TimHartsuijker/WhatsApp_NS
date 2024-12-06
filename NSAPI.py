import requests
import datetime
import urllib.request, json
from private import nsapi_key

def trytostring(value):
    try:
        return str(value)
    except:
        return ""

try:
    n = trytostring(datetime.datetime.now(datetime.timezone.utc).isoformat())
    lang = "nl"
    station = None
    uicCode = "8400058"
    dateTime = n
    maxJourneys = "40"
    url = "https://gateway.apiportal.ns.nl/reisinformatie-api/api/v2/arrivals?lang=" + lang + "&uicCode=" + uicCode + "&dateTime=" + dateTime + "&maxJourneys=" + maxJourneys + ""

    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': nsapi_key,
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    print(response.getcode())
    print("----------------------------------------------------------------------------------------------------")
    print(response.info())
    print("----------------------------------------------------------------------------------------------------")
    print(response.read())
    info = {
        "allinfo": json.loads(response.read())
        }
    with open("info.json", "w") as outfile:
        json.dump(info, outfile)
except Exception as e:
    print(e)