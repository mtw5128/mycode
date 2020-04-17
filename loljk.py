#!/usr/bin/python3
import requests

### CHALLENGE 1: CHANGE THIS SCRIPT SO THAT A USER MAY INPUT WHAT POKEMON THEY WANT TO VIEW.
### CHALLENGE 2: USING A WHILE LOOP, FORCE THE USER TO RE-ENTER THE POKEMON'S NAME IF THEY CREATE A BOGUS URL.

CHOICE = input("Which Pokemon would you like to research? (Enter Name or Dex# ex - Bulbasaur or 1): ").lower().strip()
FULL = 'https://pokeapi.co/api/v2/pokemon/' + CHOICE + '/'
URL = FULL


def url():

    # Using the requests library, pull a Pokemon from the PokeAPI
    poke_api = requests.get(URL)
    poke_api = poke_api.json() # poke_api is the translated API
    return poke_api


def main():
    poke_api= url()
    print(str(poke_api["forms"][0]["name"]).capitalize(), ", I CHOOSE YOU!\n")

    games= []


main()
