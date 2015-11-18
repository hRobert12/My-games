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

def goToHomescreen():
    print("[p]lay")
    print("[o]ptions")
    print("[q]uit")
    return input("/n")

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

while True:
    inp = goToHomescreen()
    while get_inp
        if inp == p
            while True:
                print("Please use numbers (without decimals) when inputing")
                inp = inputnumber()
                if checknumber(inp):
                    ntg = random.randint(minn, maxn)
                    trys = 0
                    break
                else:
                    trys = trys + 1
        if inp == o
            """does't do anything"""
        if inp == q
            sys.exit()
