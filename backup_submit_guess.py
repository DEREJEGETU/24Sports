#!/usr/bin/env python3
import requests
import getpass

BASE_URL = "https://9n52ntmq97.execute-api.us-east-1.amazonaws.com/prod"
REQUEST_URL = "{base_url}/guess".format(base_url=BASE_URL)
WRONG = {
    "Arizona Cardinals": 1,
    "Atlanta Falcons": 2,
    "Baltimore Ravens": 3,
    "Buffalo Bills": 6,
    "Carolina Panthers": 7,
    "Chicago Bears": 8, #67174400
    "Cincinnati Bengals": 9,
    "Cleveland Browns": 10, #75300864
    "Dallas Cowboys": 24248320,
    "Denver Broncos": 13,
    "Detroit Lions": 71630848,
    "Green Bay Packers": 24444928,
    "Houston Texans": 17,
    "Indianapolis Colts": 18,
    "Jacksonville Jaguars": 19,
    "Kansas City Chiefs": 21,
    "Los Angeles Chargers": 22,
    "Los Angeles Rams": 23,
    "Miami Dolphins": 24,
    "Minnesota Vikings": 26,  #69664768
    "New England Patriots": 27,
    "New Orleans Saints": 25624576,
    "New York Giants": 29,
    "New York Jets": 30,
    "Oakland Raiders": 25100288,
    "Philadelphia Eagles": 25165824,
    "Pittsburgh Steelers": 35,
    "San Francisco 49ers": 36,
    "Seattle Seahawks": 2490368,
    "Tampa Bay Buccaneers": 40,
    "Tennessee Titans": 41,
    "Washington Redskins": 45,
}

# Super sneak. Good luck!! Does not include scout. 32 correct
RIGHT = {
    'CowboysHQ.com': 'MzAwMTExNjYzOA==',
    'Philadelphia Eagles': 'MzIyNTI1MTY1ODI0ODEwNQ==',
    'Atlanta Falcons': 'MzYyMzIzNzg5NTY4ODA0NA==',
    'Cincinnati Bengals': 'MzU5NDI0MTE3MjQ4NDc2Mg==',
    'New York Giants': 'NDI3NjI0OTY5MjE2NDQyNw==',
    'Detroit Lions': 'ODQzNTI0Mzc5MzkyNzE3OA==',
    'TheGiantsBeat.com': 'ODQyMTQyMzU5NQ==',
    'Indianapolis Colts': 'MTE2ODI0NTc2MDAwMjQ5Mg==',
    'Seattle Seahawks': 'MTM2NDI0OTAzNjgxMzU4',
    'Arizona Cardinals': 'NjMyNDIzNzI0MDMyODk1MA==',
    'Houston Texans': 'MzYwODI0NTEwNDY0NzMzNQ==',
    'Tennessee Titans': 'NzUwNzIwOTcxNTIzOTQ1',
    'MileHighHuddle.com': 'Mzc5ODI1MjI1Ng==',
    'Jacksonville Jaguars': 'ODk4MjI0NjQxNTM2NzQxNg==',
    'Chicago Bears': 'MzA5NTI0MDUxNzEyNDQ5OQ==',
    'Baltimore Ravens': 'MzQ3OTIzODU1MTA0NzE4MQ==',
    'theOBR.com': 'OTQxNzQzNjY2Mg==',
    'Green Bay Packers': 'MTcwOTI0NDQ0OTI4MTY2MA==',
    'BreakingBurgundy.com': 'OTk0NTUxMzI5',
    'New Orleans Saints': 'NDEzMDI1NjI0NTc2NjExNQ==',
    'Pittsburgh Steelers': 'NTA1MDI1MjMxMzYwMzk1Ng==',
    'New England Patriots': 'NTU1MDI0OTAzNjgwMTkwOA==',
    'PatriotsInsider.com': 'NjE5MDMzNzEwNA==',
    'Tampa Bay Buccaneers': 'MTUzNTI1NjkwMTEyMTk3NQ==',
    'PackerReport.com': 'Mjg0OTMyMzgwMg==',
    'Cleveland Browns': 'MTg5MzI0MTgyNzg0ODk1MQ==',
    'VikingUpdate.com': 'Njg5MjQ0NzU1Ng==',
    'DolphinsReport.com': 'MjYwMjE1MjIwMA==',
    'Oakland Raiders': 'MTM4OTI1MTAwMjg4NTM5Ng==',
    'Buffalo Bills': 'NTAyMDIzOTIwNjQwODMzMg==',
    'StateoftheTexans.com': 'NDI3NTM4NTE3NQ==',
    'Los Angeles Chargers': 'NTY0NzI1Mjk2ODk2OTc2Ng==',
    'Carolina Panthers': 'MjgwNzIzOTg2MTc2MzA2Mg==',
    'San Francisco 49ers': 'OTcwMjI1MzYyNDMyODgwMA==',
    'Washington Redskins': 'Nzg0NzI1NDkzNTA0MTcxOA==',
    'Los Angeles Rams': 'OTAyODI1NDI3OTY4NTk2NQ==',
    'Miami Dolphins': 'ODMwOTI0NzcyNjA4Nzk5Mg==',
    'BearReport.com': 'NTA3OTQ0ODMz',
    'New York Jets': 'MzM1MzI1MDM0NzUyMTk4NQ==',
    'JaguarsForever.com': 'NzI3NzIwODM0MA==',
    'Kansas City Chiefs': 'OTM1NjI0NzA3MDcyNTczMQ==',
    'SteelCityInsider.net': 'ODA3OTM5NjA2OQ==',
    'Denver Broncos': 'NTk1MDI0MzEzODU2OTA3OA==',
    'Minnesota Vikings': 'MTk3MDI0ODM4MTQ0ODQ4Ng==',
    'Dallas Cowboys': 'MzIwNzI0MjQ4MzIwOTY1Ng=='
}


def submit_request(guess, username):
    print("Submitting guess!")
    resp = requests.post(REQUEST_URL, json={
        "results": guess,
        "username": username
    })
    print(resp.text)


if __name__ == '__main__':
    submit_request(RIGHT, 'pythons')