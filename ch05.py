#!/usr/bin/python3

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


#print(f"My " + nightmare[0]["user"]["name"]["first"] + "! The " + nightmare[0]["kumquat"] + " do " + nightmare[0]["d"] + "!")

#print(f"My {nightmare[0]['user']['name']["first"]}! The {nightmare[0]["kumquat"]} do {nightmare[0]["d"]}!")

print(f"My {nightmare[0]['user']['name']['first']}! The {nightmare[0]['kumquat']} do {nightmare[0]['d']}!")
