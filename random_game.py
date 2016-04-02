"""
Created on Fri Nov  6 16:58:12 2015

@author: Robert
"""

import random
import dbm
import pickle
import sys

inp = 0
trys = 1
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
    try:
        load1 = int(load1)
        load2 = int(load2)
    except ValueError:
        print("Opps... something went wrong, you may have inserted the word for the number instead of the number itself")
        print("Please re-download this program to fix this problem; the program will now close.")
        input("")
        sys.exit()
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
try:
    maxn, minn = load()
    
    while get_inp:
        print("[P]lay")
        print("[O]ptions")
        print("[Q]uit")
        print("Type your pick in lower-case")
        inp = input("")
        if inp == "p":
            ntg = random.randint(minn, maxn)
            while inp != ntg:
                inp = inputnumber()
                if checknumber(inp):
                    ntg = random.randint(minn, maxn)
                    trys = 1
                    break
                else:
                    trys = trys + 1
            get_inp = True
        elif inp == "o":
            while get_inp:
                print("[A]just min and max")
                print("[L]oad min and max")
                print("[Q]uit options")
                print("Type your pick in lower-case")
                inp = input("")
                if inp == "a":
                    minn = input("Type min: ")
                    maxn = input("Type max: ")
                    save()
                    maxn = int(maxn)
                    minn = int(minn)
                if inp == "l":
                    maxn, minn = load()
                if inp == "q":
                    break
        elif inp == "q":
            break
except:
    print("Uh-oh, something went wrong. If you see this error for the first time, then please re-start the program.")
    print("Otherwise, please re-insall the program.")
    input("")
