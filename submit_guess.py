#!/usr/bin/env python3
import requests
import getpass

BASE_URL = "https://9n52ntmq97.execute-api.us-east-1.amazonaws.com/prod"
REQUEST_URL = "{base_url}/guess".format(base_url=BASE_URL)
WRONG = {
    "Arizona Cardinals": 23724032,
    "Atlanta Falcons": 23789568,
    "Baltimore Ravens": 23855104,
    "Buffalo Bills": 23920640,
    "Carolina Panthers": 23986176,
    "Chicago Bears": 24051712,          #67174400 wrong
    "Cincinnati Bengals": 24117248,
   "Cleveland Browns": 24182784,      #75300864 wrong
    "Dallas Cowboys": 24248320,
    "Denver Broncos": 24313856,
    "Detroit Lions": 24379392,        #71630848 wrong
    "Green Bay Packers": 24444928,
    "Houston Texans": 24510464,
    "Indianapolis Colts": 24576000,
    "Jacksonville Jaguars": 24641536,
    "Kansas City Chiefs": 24707072,
    "Los Angeles Chargers": 25296896,
    "Los Angeles Rams": 25427968,
    "Miami Dolphins": 24772608,       #69599232
    "Minnesota Vikings": 24838144,    #69664768 wrong ????
    "New England Patriots": 24903680,
    "New Orleans Saints": 25624576,
    "New York Giants": 24969216,
    "New York Jets": 25034752,        #75300864 wrong
    "Oakland Raiders": 25100288,
    "Philadelphia Eagles": 25165824,
    "Pittsburgh Steelers": 25231360,      #69992448 wrong
    "San Francisco 49ers": 25362432,
    "Seattle Seahawks": 2490368,
    "Tampa Bay Buccaneers": 25690112,
    "Tennessee Titans": 2097152,
    "Washington Redskins": 25493504,
}


def submit_request(guess, username):
    print("Submitting guess!")
    resp = requests.post(REQUEST_URL, json={
        "results": guess,
        "username": username
    })
    print(resp.text)


if __name__ == '__main__':
    print("Submitting guess for {} teams".format(len(WRONG)))
    submit_request(WRONG, getpass.getuser())
