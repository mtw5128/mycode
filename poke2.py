#!/usr/bin/python3


#import numpy as np
import cv2
#import urllib.request
#import json
import requests


#mon = input('Enter a Pokemon\'s name! ')


# Define URL

CHOICE = input("Which Pokemon would you like to research? (Enter Name or Dex#, ex- Blastoise or 9): ").lower().strip()
URL = 'https://pokeapi.co/api/v2/pokemon/' + CHOICE + '/'


#print(URL)

# function for pulling API
def url():

    # Using the requests library, pull a Pokemon from the PokeAPI
    poke_api = requests.get(URL)
    poke_api = poke_api.json() # poke_api is the translated API
    return poke_api

# function for Calling the mon
def main():

    poke_api= url()
    print(str(poke_api["forms"][0]["name"]).capitalize(), ", I CHOOSE YOU!\n")

# stats
def research():
    poke_api = requests.get(fr'https://pokeapi.co/api/v2/pokemon/{CHOICE}/')
    poke_api = poke_api.json()
    print("Pokemon: " + str(poke_api["forms"][0]["name"]))
    print("Health: ", poke_api["stats"][5]["base_stat"])
    print("Attack: ", poke_api["stats"][4]["base_stat"])
    print("Defense: ", poke_api["stats"][3]["base_stat"])
    print("Special Attack: ", poke_api["stats"][2]["base_stat"])
    print("Special Defense: ", poke_api["stats"][1]["base_stat"])
    print("Speed: ", poke_api["stats"][0]["base_stat"])

# function for sprites
def pic():

    img = cv2.imread(fr"C:\Users\Student\Desktop\pokemon\{CHOICE}.png",0)
    # Output img with window name 'x'
    cv2.imshow('Pokemon', img)
    cv2.namedWindow('Pokemon',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Pokemon',175,70)
    # Maintain output window until user presses key
    cv2.waitKey(0)
    # Destroying present windows on screen
    cv2.destroyAllWindows()




# might use as a frame
#print(str(poke_api["forms"][0]["name"]).capitalize(), "appears in the following Pokemon games:\n")
    #for x in poke_api["game_indices"]:
        #version= x["version"]["name"]
        #print(str(version).capitalize())


url()
main()
research()
pic()

