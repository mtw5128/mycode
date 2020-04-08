#!/usr/bin/env python3

# create the list called vendors

vendors = ["cisoc", "juniper", "big_ip", "f5", "arista"]

# create 2nd list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]

# loop across the list vendors

for x in vendors:
    print("The vendor is: " + x)  # each time thru loop print value of x
    if x not in approved_vendors:   # if x does not appear in list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")



print("\nOur loop has ended.") # when loop ends print this


