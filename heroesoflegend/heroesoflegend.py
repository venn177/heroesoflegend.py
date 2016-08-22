#! python3
import random
from random import randint
from rolltables import *

# This is the random choice initializer functions

def generate():
    charRace = random_choice(raceTable101)
    if charRace == 'other races':
        charRace = random_choice(raceTable101a)
    charCulture = random_choice(cultureTable102)
    cuMod = cultureTable102a(charCulture)
    tiMod = 0
    global charSocial
    global charAdopted
    global solMod
    charAdopted = False
    charSocial, solMod, nobleTitle, tiMod = socialTable103(cuMod, tiMod, charCulture)
    legitBirth = birthTable104(cuMod)
    if legitBirth == False:
        if cuMod >= 0:
            cuMod = cuMod - randint(1,4)
        illegitReason = illegitBirthTable105(cuMod)
        illegitBirth = 'Birth was illegitimate. Cause: ' + illegitReason + '.'
    charFamily, charAdopted = familyTable106(cuMod)
    if charAdopted == True:
        charFamily = '(adopted) ' + str(charFamily)
    siblingMale, siblingFemale, birthOrder = siblingsTable107()
    birthSeason, birthTimeOfDay = birthTimeTable109()
    placeOfBirth, biMod = placeOfBirthTable110()
    birthOccurance, unusualBirth = unusualBirthTable112(biMod)
    if unusualBirth == True:
        birthOccurance = ", ".join(birthOccurance)
    #shit about parents go hurr
    hohOccupation = parentTable114a(charCulture, solMod)
    childhoodEvents, adolescentEvents = childhoodEventsTable215a(solMod)
    childhoodEvents = capitalize_shit(childhoodEvents)
    adolescentEvents = capitalize_shit(adolescentEvents)
    childhoodEvents = " | ".join(childhoodEvents)
    adolescentEvents = " | ".join(adolescentEvents)
    adulthoodEvents = adulthoodSignificantEventsTable217(charSocial, solMod, charCulture)
    adulthoodEvents = capitalize_shit(adulthoodEvents)
    adulthoodEvents = " | ".join(adulthoodEvents)
    return('Race: ' + charRace + ' | Culture: ' + charCulture + ' | Social Standing: ' + charSocial + ((' | Title: ', "")[nobleTitle == ""]) + nobleTitle + "\nFamily: " + str(charFamily) + '.\n' +
    'Birth: In ' + birthSeason + ' at ' + birthTimeOfDay + ' ' + placeOfBirth + '.' +
    ('Birth Circumstances: ' + birthOccurance.capitalize() if unusualBirth == True else '' ) + (illegitBirth if legitBirth == False else '') + '\n' +
    'Siblings: ' + ('None' if siblingMale == 'none' else str(siblingMale) + ' male' + (('s', '')[siblingMale == 1]) + ' and ' + str(siblingFemale) + ' female' + (('s', '')[siblingFemale == 1]) + ', of which the character is the ' + birthOrder + '.') + '\n' +
    'Parents Info: ' + hohOccupation + '\n' +
    'Childhood: ' + childhoodEvents + "\n" +
    'Adolescence: ' + adolescentEvents + '\n' +
    'Adulthood: ' + adulthoodEvents
    )

def main():
    print(generate())

def capitalize_shit(array): #I don't feel like re-writing everything from lower-case in the rolltables, so fuck it. Here.
    for i in range(len(array)):
        array[i] = array[i].capitalize()
    return array

if __name__ == "__main__":
    main()
