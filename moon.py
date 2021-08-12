import requests
import json

#### Gets Moon Rankings from Reddit API Page ####
#### Returns JSON list with Moon Rankings ####
def getmoons():
    url = 'https://meta-api.reddit.com/ratings/t5_2wlj3/points-monthly'
    parameters = {
            'start':'1',
            'limit':'10',
            }
    headers = {
        'Accepts': 'application/json'
        }
    session = requests.Session()
    session.headers.update(headers)

    try:
        r = session.get(url, params=parameters)
        j = r.json()
        with open('cachedmoons.json', 'w') as f:
            json.dump(j, f)
    except:
        print("Failed to get MOON via API")
        with open('cachedmoons.json', 'r') as f:
            j = f.read().json()
    return j

#### Gets Moon Totals from Reddit API Page ####
#### Returns JSON list Moon Totals ####
def gettotal():
    url = 'https://meta-api.reddit.com/communities/t5_2wlj3/me'
    parameters = {
            'start':'1',
            'limit':'10',
            }
    headers = {
        'Accepts': 'application/json'
        }
    session = requests.Session()
    session.headers.update(headers)

    try:
        r = session.get(url, params=parameters)
        j = r.json()
        with open('cachedtotal.json', 'w') as f:
            json.dump(j, f)
    except:
        print("Failed to get TOTAL via API")
        with open('cachedtotal.json', 'r') as f:
            j = f.read().json()
    return j