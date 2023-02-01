# This is necessary to find the main code
import sys
sys.path.insert(0, '../../bomberman')
sys.path.insert(1, '..')

# Import necessary stuff
import random
from game import Game
from monsters.stupid_monster import StupidMonster

# TODO This is your code!
sys.path.insert(1, '../teamNN')
from testcharacter import TestCharacter

# Create the game
random.seed(567) # TODO Change this if you want different random choices 
g = Game.fromfile('map.txt')
g.add_monster(StupidMonster("stupid", # name
                            "S",      # avatar
                            3, 9      # position
))

# TODO Add your character
g.add_character(TestCharacter("me", # name
                              "C",  # avatar
                              0, 0  # position
))

# Use this if you want to press ENTER to continue at each step
# g.go(0)

# Use this if you want to proceed automatically
g.go(1)
