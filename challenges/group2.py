#!/usr/bin/python3

import requests

CHOICE = input("Which Pokemon would you like to research? (Enter Name or Dex#, ex- Blastoise or 9): ").lower().strip()
URL = 'https://pokeapi.co/api/v2/pokemon/' + CHOICE + '/'



def research():
    count = 0
    poke_api = requests.get(fr'https://pokeapi.co/api/v2/pokemon/{CHOICE}/')
    poke_api = poke_api.json()
    print("Pokemon: " + str(poke_api["forms"][0]["name"]))
    print("Sprite: " + str(poke_api["sprites"]["front_default"]))


research()
