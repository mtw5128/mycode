#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests


r = requests.get('https://cat-fact.herokuapp.com/facts')
def main():
    """Run time code"""
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    for catfact in r.json()["all"]:
        print(catfact.get("text"))  # the .get() method returns NONE if key not found


def random_facts():
    fact_list = []
    for x in r.json()["all"]:
        fact_list.append(x.get("text"))



random_facts()
#main()

