import requests

url = "https://api-football-v1.p.rapidapi.com/v3/teams/countries"

headers = {
        "X-RapidAPI-Key": "**********************************",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

file = open("out_countries.csv", "wb")
file.write(response.content)
file.close()
