#!/usr/bin/python3
import requests

### CHALLENGE 1: CHANGE THIS SCRIPT SO THAT A USER MAY INPUT WHAT POKEMON THEY WANT TO VIEW.
### CHALLENGE 2: USING A WHILE LOOP, FORCE THE USER TO RE-ENTER THE POKEMON'S NAME IF THEY CREATE A BOGUS URL.

#CHOICE = input("Which Pokemon would you like to research? (Enter Name or Dex# ex - Bulbasaur or 1): ").lower().strip()
#URL = 'https://pokeapi.co/api/v2/pokemon/' + CHOICE + '/'


def url():
    while True:
        try:
            CHOICE = input("Which Pokemon would you like to research? (Enter Name or Dex# ex - Bulbasaur or 1): ").lower().strip()
            URL = 'https://pokeapi.co/api/v2/pokemon/' + CHOICE + '/' 
            # Using the requests library, pull a Pokemon from the PokeAPI
            poke_api = requests.get(URL)
            poke_api = poke_api.json() # poke_api is the translated API
            if CHOICE == "":
                raise ValueError("Invalid Entry!")
            break
        except:
            print("Invalid Entry!")

    return poke_api
        

def main():
    poke_api= url()
    print(str(poke_api["forms"][0]["name"]).capitalize(), ", I CHOOSE YOU!\n")

    games= []

### CHALLENGE 3: ADD A WHILE LOOP THAT FORCES THE USER TO KEEP GUESSING UNTIL THEY GET THE ANSWER CORRECT!
    while True:

        for x in poke_api["game_indices"]:
            version= x["version"]["name"]
            games.append(version)

        guess= input("Guess one Pokemon game version this Pokemon was in! ")
        if guess in games:
            print("Correct!")
            break
        else:
            print("Wrong!")

main()
