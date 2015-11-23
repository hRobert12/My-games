"""
Created on Fri Nov  6 16:58:12 2015

@author: Robert
"""

import random
import dbm
import pickle
import sys

inp = 0
trys = 0
minn = 0
maxn = 0
get_inp = True
ntg = 0

def save():
    dump1 = pickle.dumps(minn)
    dump2 = pickle.dumps(maxn)
    dbs = dbm.open("save.db", "c")
    dbs["min"] = dump1
    dbs["max"] = dump2

def load():
    dbs = dbm.open("save.db", "c")
    load1 = pickle.loads(dbs["max"])
    load2 = pickle.loads(dbs["min"])
    return [load1, load2]

def inputnumber():
    print("Please type a number between %s and %s" % (minn, maxn))
    return int(input("Type number here: "))
    
def checknumber(number):
    if inp > ntg:
        print("Try lower")
        return False
    if inp < ntg:
        print("Try higher")
        return False
    if inp == ntg:
        print("Good job, you took %s try(s), press enter..." % trys)
        input()
        return True

get_inp = True

while get_inp:
    print("[P]lay")
    print("[O]ptions")
    print("[Q]uit")
    print("Type your pick in lower-case")
    inp = input("/n")
    if inp == p
        """Play"""
        get_inp = False
    elif inp == o
        """Options"""
        get_inp = False
    elif inp == q
        sys.exit()
    else
        print("Invald input")
