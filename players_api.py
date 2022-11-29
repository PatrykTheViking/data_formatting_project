import time

import requests

url = "https://api-football-v1.p.rapidapi.com/v3/players/squads"

headers = {
            "X-RapidAPI-Key": "**********************************",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

counter = 1

while counter <= 32:
    file = open(f"out_players_{counter}.json", "wb")
    querystring = {"team": f"{counter}"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    file.write(response.content)
    counter += 1
    print("Currently processing {0} team number".format(counter))
    file.close()
    time.sleep(60)
