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
    global charAdopted
    global charsocial
    charAdopted = False
    charSocial, solMod, nobleTitle, tiMod = socialTable103(cuMod, tiMod, charCulture)
    if nobleTitle == '':
        nobleTitle = 'None'
    legitBirth = birthTable104(cuMod)
    if legitBirth == False:
        if cuMod >= 0:
            cuMod = cuMod - randint(1,4)
        illegitReason = illegitBirthTable105(cuMod)
        print('Birth was illegitimate. Cause: ' + illegitReason)
    charFamily = familyTable106(cuMod)
    if charAdopted == True:
        charFamily += ' (adopted)'
    print('Race: ' + charRace + ', Culture: ' + charCulture + ', Social Standing: ' + charSocial + ', Title: ' + nobleTitle + "\nFamily: " + str(charFamily))
    siblingMale, siblingFemale, birthOrder = siblingsTable107()
    if siblingMale == 'none':
        print('Siblings: None')
    else:
        print('Siblings: ' + str(siblingMale) + ' male' + (('s', '')[siblingMale == 1]) + ' and ' + str(siblingFemale) + ' female' + (('s', '')[siblingFemale == 1]) + ', of which the character is the ' + birthOrder)

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
