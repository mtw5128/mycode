#!/usr/bin/env python3

import netifaces



for i in netifaces.interfaces():

    print('\n**************Details of Interface - ' + i + ' *********************')
    try:  # this is a new line, you also need to indent code below
        print('MAC: ', end="")
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # prints MAC
        print('IP: ', end="")
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # prints IP
        
    except:      # this is a new line
        print('Could not collect adapter information') # Error msg


