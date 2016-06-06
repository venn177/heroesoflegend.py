import random
from random import randint
from rolltables import *

# This is the random choice initializer functions

def main():
    charRace = random_choice(raceTable101)
    if charRace == 'other races':
        charRace = random_choice(raceTable101a)
    charCulture = random_choice(cultureTable102)
    cuMod = cultureTable102a(charCulture)
    tiMod = 0
    charSocial, solMod, nobleTitle, tiMod = socialTable103(cuMod, tiMod, charCulture)
    if nobleTitle == '':
        nobleTitle = 'no title'
    legitBirth = birthTable104(cuMod)
    if legitBirth == False:
        if cuMod >= 0:
            cuMod = cuMod - randint(1,4)
        illegitReason = illegitBirthTable105(cuMod)
        print('Birth was illegitimate. Cause: ' + illegitReason)
    charFamily = familyTable106(cuMod)
    if charAdopted == True:
        charFamily += ' (adopted)'


    print(charRace + ' ' + charCulture + ' (' + str(cuMod) + ')' + ' ' + charSocial + ' (' + str(solMod) + ') ' + nobleTitle + ' (' + str(tiMod) + ')')


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
