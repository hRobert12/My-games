# -*- coding: utf-8 -*-

import sys

while True:
    inp = input("What do you want to play")
    if inp == "randgame":
        import random_game
    if inp == "quit":
        sys.exit()
