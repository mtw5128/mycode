#!/usr/bin/python3

# Python program to read image using OpenCV

# importing OpenCV(cv2) module
import numpy as np
import cv2

mon = input('Enter a Pokemon\'s name! ')


def pic():
    # Save image in set directory
    # Read RGB image
    img = cv2.imread(fr"C:\Users\Student\Desktop\pokemon\{mon}.png",0)

    # Output img with window name as 'image'
    cv2.imshow('image', img)

    # Maintain output window util
    # user presses a key
    cv2.waitKey(0)

    # Destroying present windows on screen
    cv2.destroyAllWindows()

pic()
