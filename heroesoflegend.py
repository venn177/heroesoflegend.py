import random
from random import randint
from rolltables import *

# This is the random choice initializer functions

def main ():
    charRace = random_choice(raceTable101)
    print(charRace)

def random_choice_index(chances):
	dice = randint(1, sum(chances))
	running_sum = 0
	choice = 0
	for w in chances:
		running_sum += w
		if dice <= running_sum:
			return choice
		choice += 1

def random_choice(chances_dict):
	chances = chances_dict.values()
	strings = list(chances_dict.keys())
	return strings[random_choice_index(chances)]


if __name__ == "__main__":
    main()
