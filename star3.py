#!/usr/bin/env python3

stars = open("star.txt", "r")

starlist = stars.readlines()

for x in starlist:
    
    print(x, end="")

stars.close()
