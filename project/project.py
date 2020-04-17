#!/usr/bin/python3

import time
import numpy as np
import sys

#name prompt with delay
time.sleep(1)
name = input("First, what is your name?: ")
print(f'Great! Your name is {name}!')


pokemon1 = {'name': 'Venusaur', 'attack': 25, 'heal': 20}
lists = ["pokemon1", "pokemon2", "pokemon3"]


choice = (f'\nSo, {name}... Which Pokemon do you choose?!')
print(lists)
print(pokemon1['name'])

