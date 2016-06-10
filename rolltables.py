from random import randint
from heroesoflegend import random_choice, random_choice_index
'''
This is an easy copy/paste for creating dicts:
Table = {
    '': ,
    '': ,
    '': ,
    '': ,
    '': ,
    '': ,
    '': ,
    '':
}
'''

raceTable101 = {
    'Human': 14,
    'Elf': 2,
    'Dwarf': 1,
    'Halfling': 1,
    'Half Elf': 1,
    'other races': 1
}

raceTable101a = {
    'Beastman': 3,
    'Reptileman': 2,
    'Orc': 1,
    'Half-Orc': 4
}

cultureTable102 = {
    'Primitive': 1,
    'Nomad': 2,
    'Barbarian': 3,
    'Civilized': 3,
    'Civilized-decadent': 1
}

def cultureTable102a(culture):
    if culture == 'Primitive':
        return(-3)
    elif culture == 'Nomad':
        return(0)
    elif culture == 'Barbarian':
        return(2)
    elif culture == 'Civilized':
        return(4)
    elif culture == 'Civilized-decadent':
        return(7)

def socialTable103(cuMod, tiMod, charCulture):
    rand = randint(1,100) + cuMod + tiMod
    if rand <= 12:
        return('Destitute', -3, '', 0)
    elif rand <= 40:
        return('Poor', -1, '', 0)
    elif rand <=84:
        return('Comfortable', 0, '', 0)
    elif rand == 85:
        socialTable103(0, tiMod, charCulture)
    elif rand <= 96:
        return('Well-to-do', 2, '', 0)
    elif rand <= 98:
        rand = randint(1,100)
        if rand <= tiMod + 1:
            return('Extremely Wealthy', 8, '', 0)
        else:
            return('Wealthy', 4, '', 0)
    elif rand >= 99:
        if charCulture == 'Primitive':
            nobleTitle = random_choice(nobleTable758prim)
        elif charCulture == 'Nomad':
            nobleTitle = random_choice(nobleTable758nomad)
        elif charCulture == 'Barbarian':
            nobleTitle = random_choice(nobleTable758barb)
        else:
            nobleTitle = random_choice(nobleTable758civil)
        tiMod = nobleTable758tiMod(nobleTitle)
        # 103a is exactly like 103 but iterates at 99+ rands. Not necessary, but slightly cleaner on debug printing. Otherwise I could just keep iterating through 103 until it didn't roll into circles.
        return socialTable103a(cuMod, tiMod, charCulture, nobleTitle)
    else:
        raise ValueError("You shouldn't ever be able to see this error on socialTable103.")

def socialTable103a(cuMod, tiMod, charCulture, nobleTitle):
    rand = randint(1,100) + cuMod + tiMod
    if rand <= 12:
        return('Destitute', -3, nobleTitle, tiMod)
    elif rand <= 40:
        return('Poor', -1, nobleTitle, tiMod)
    elif rand <=84:
        return('Comfortable', 0, nobleTitle, tiMod)
    elif rand == 85:
        return socialTable103a(0, tiMod, charCulture, nobleTitle)
    elif rand <= 96:
        return('Well-to-do', 2, nobleTitle, tiMod)
    elif rand <= 98:
        rand = randint(1,100)
        if rand <= tiMod + 1:
            return('Extremely Wealthy', 8, nobleTitle, tiMod)
        else:
            return('Wealthy', 4, nobleTitle, tiMod)
    elif rand >= 99:
        return socialTable103a(cuMod, tiMod, charCulture, nobleTitle)

def birthTable104(cuMod):
    rand = randint(1,20) + cuMod
    if rand >= 19:
        return(False)

def illegitBirthTable105(cuMod):
    rand = randint(1,20) + cuMod
    if rand <= 12:
        return 'mother was a common prostitute, unmarried'
    if rand <= 14:
        return 'mother was raped and remained unmarried'
    if rand <= 23:
        return 'mother was unmarried'
    if rand <= 27:
        return 'mother was a courtesan'

def familyTable106(cuMod):
    rand = randint(1,20) + cuMod
    if rand <= 8:
        return 'mother and father only'
    elif rand <= 12:
        return 'extended family. mother and father, along with ' + str(randint(1,4)) + ' grandparents and ' + str(randint(1,4)) + ' aunts/uncles and cousins'
    elif rand <= 13:
        rand = randint(1,2)
        if rand > 1:
            return "grandparents on father's side"
        else:
            return "grandparents on mother's side"
    elif rand <= 14:
        rand = randint(1,2)
        if rand > 1:
            return "single grandparent on mother's side"
        else:
            return "single grandparent on father's side"
    elif rand <= 15:
        rand = randint(1,2)
        if rand > 1:
            return "single aunt or uncle on father's side"
        else:
            return "single aunt or uncle on mother's side"
    elif rand <= 16:
        rand = randint(1,2)
        if rand > 1:
            rand = randint(1,2)
            if rand > 1:
                return "aunt on father's side"
            else:
                return "aunt on mother's side"
        else:
            rand = randint(1,2)
            if rand > 1:
                return "uncle on father's side"
            else:
                return "uncle on mother's side"
    elif rand <= 18:
        return "only a mother"
    elif rand <= 19:
        return "only a father"
    elif rand <= 20:
        global charAdopted
        charAdopted = False
        rand = randint(1,20)
        if rand <= 8:
            return guardiansTable754(cuMod)
        else:
            charAdopted = True
            return familyTable106a(cuMod)
    elif rand <= 24:
        global charSocial
        charSocial = 'destitute'
        return 'none, left to fend for yourself'
    elif rand <= 27:
        global charSocial
        charSocial = 'poor'
        return 'none, raised in an orphanage'
    else:
        raise ValueError("familyTable106 is reporting a randint error for some weird fucking reason. This shouldn't be possible.")

def familyTable106a(cuMod):
    rand = randint(1,20) + cuMod
    if rand <= 8:
        return 'mother and father only'
    elif rand <= 12:
        return 'extended family. mother and father, along with ' + str(randint(1,4)) + ' grandparents and ' + str(randint(1,4)) + ' aunts/uncles and cousins'
    elif rand <= 13:
        rand = randint(1,2)
        if rand > 1:
            return "grandparents on father's side"
        else:
            return "grandparents on mother's side"
    elif rand <= 14:
        rand = randint(1,2)
        if rand > 1:
            return "single grandparent on mother's side"
        else:
            return "single grandparent on father's side"
    elif rand <= 15:
        rand = randint(1,2)
        if rand > 1:
            return "single aunt or uncle on father's side"
        else:
            return "single aunt or uncle on mother's side"
    elif rand <= 16:
        rand = randint(1,2)
        if rand > 1:
            rand = randint(1,2)
            if rand > 1:
                return "aunt on father's side"
            else:
                return "aunt on mother's side"
        else:
            rand = randint(1,2)
            if rand > 1:
                return "uncle on father's side"
            else:
                return "uncle on mother's side"
    elif rand <= 18:
        return "only a mother"
    elif rand <= 19:
        return "only a father"

def siblingsTable107():
    rand = randint(1,19) #support for 20, just not implementing yet
    if rand <= 2:
        return 'none', '', ''
    elif rand <= 9:
        rand = randint(1,3)
    elif rand <= 15:
        rand = randint(2,4)
    elif rand <= 17:
        rand = randint(3,6)
    elif rand <= 19:
        rand = randint(2,8)
    #elif rand <= 20:
    return siblingsTable107a(rand)

def siblingsTable107a(number): # I rolled table 108 into this one because I got kinda caught up in the speed I was going. Eh, fuck it for now.
    siblingMale = 0
    siblingFemale = 0
    for i in range(number):
        rand = randint(1,20)
        if rand <= 9:
            siblingMale += 1
        else:
            siblingFemale += 1
    totalSiblings = siblingMale + siblingFemale
    birthOrder = ""
    if totalSiblings == 2:
        rand = randint(1,2)
        if rand == 1:
            birthOrder = 'first born'
        else:
            birthOrder = 'last born'
    elif totalSiblings == 2:
        rand = randint(1,3)
        if rand == 1:
            birthOrder = 'first born'
        elif rand == 2:
            birthOrder = 'middle born'
        else:
            birthOrder = 'last born'
    else:
        rand = randint(1,20)
        if rand <= 2:
            birthOrder =  'first born'
        elif rand <= 10:
            birthOrder =  'second born'
        elif rand <= 16:
            birthOrder =  'middle born'
        elif rand <= 18:
            birthOrder =  'second-to-last born'
        elif rand <= 20:
            birthOrder =  'last born'
    return siblingMale, siblingFemale, birthOrder

#note to me: I rolled 108 into 107a, that's why it's not here. I know I'll forget this.

def birthTimeTable109():
    rand = randint(1,4)
    if rand == 1:
        birthSeason = 'spring'
    elif rand == 2:
        birthSeason = 'summer'
    elif rand == 3:
        birthSeason = 'autumn'
    elif rand == 4:
        birthSeason = 'winter'

    rand = randint(1,8)
    if rand == 1:
        birthTimeOfDay = 'midnight'
    elif rand == 2:
        birthTimeOfDay = 'late night'
    elif rand == 3:
        birthTimeOfDay = 'early morning'
    elif rand == 4:
        birthTimeOfDay = 'sunrise'
    elif rand == 5:
        birthTimeOfDay = 'mid-day'
    elif rand == 6:
        birthTimeOfDay = 'afternoon'
    elif rand == 7:
        birthTimeOfDay = 'sunset'
    elif rand == 8:
        birthTimeOfDay = 'early evening'

    return birthSeason, birthTimeOfDay

def placeOfBirthTable110():
    rand = randint(1,20)
    if rand <= 6:
        return 'in the family home', -5
    elif rand <= 9:
        return "in a hospital or healer's hall", -7
    elif rand <= 10:
        return 'in a carriage while traveling', 1
    elif rand <= 11:
        return 'in a common barn', 1
    elif rand <= 13:
        return 'in a foreign land', 2
    elif rand <= 14:
        return 'in a cave', 5
    elif rand <= 15:
        return 'in the middle of a field', 1
    elif rand <= 16:
        return 'in a forest', 2
    elif rand <= 24:
        return exoticBirthLocationTable111()

def exoticBirthLocationTable111():
    rand = randint(1,19) #yep, it's another one of these, I took out roll 14 due to GM-only, will consider adding back in later
    if rand <= 2:
        return  'double roll thing, will keep noted here for now', 5
    elif rand == 3:
        return 'in a temple of ' + deitiesTable864(), 5
    elif rand == 4:
        rand = randint(1,6)
        if rand == 6:
            return 'in the middle of a battlefield', 8
        else:
            return 'at a battlefield camp', 8
    elif rand == 5:
        return 'in an alley', 5
    elif rand == 6:
        return 'in a brothel', 2
    elif rand == 7:
        return 'in home of a local ruler', 2
    elif rand == 8:
        return 'home of the ruler of the country', 5
    elif rand == 9:
        return 'palace of an evil person or creature', 15
    elif rand == 10:
        return 'in a tavern', 2
    elif rand == 11:
        return 'in the sewers', 10
    elif rand == 12:
        return 'in a thieves den', 5
    elif rand == 13:
        return 'in the home of friendly nonhumans', 2
    elif rand == 14: #I know I'll be looking at this later and confused, but 14 is the one I pruned because it's set as GM ONLY
        return 'in the temple of an evil diety', 20
    elif rand == 15:
        return 'on another plane of reality', 15
    elif rand == 16:
        return 'in another time period', 10
    elif rand == 17:
        return 'on a ship at sea', 2
    elif rand == 18:
        return 'in a prison cell', 9
    elif rand == 19:
        return "in a wizard's laboratory", 20

def unusualBirthTable112(biMod): #this has been cleaned up, removing the GM selecting portions
    rand = randint(1,100) + biMod
    if rand <= 60:

    elif rand <= 76:

    elif rand <= 92:

    elif rand <= 97:

    else:

def unusualBirthCircumstancesTable113():
    rand = randint(1,100)
    if rand <= 5:
        return "a person of note near the character's home died when they were born"
    elif rand <= 10:
        return 'wolves and dogs set up a howling'
    elif rand <= 20:
        return 'mother died in childbirth'
    elif rand <= 23:
        return 'all glassware in the house shattered'
    elif rand <= 25:
        return 'all milk in the area soured'
    elif rand <= 27:
        return 'father believes the character is not his child'
    elif rand <= 31:
        rand = randint(1,5)
        return 'character has identical twin' + ((" that was separated at birth", "")[rand == 5])
    elif rand <= 34:
        return 'water froze or boiled by itself'
    elif rand <= 37:
        return 'unnatural weather occurred'
    elif rand <= 38:
        return 'unnaturally potent storms raged'
    elif rand <= 41:
        return ''
    elif rand <= 44:

    elif rand <= 47:

    elif rand <= 50:

    elif rand <= 53:

    elif rand <= 55:

    elif rand <= 56:

    elif rand <= 57:

    elif rand <= 62:

    elif rand <= 64:

    elif rand <= 69:

    elif rand <= 75:

    elif rand <= 81:

    elif rand <= 85:

    elif rand <= 86:

    elif rand <= 88:

    elif rand <= 93:

    elif rand <= 94:

    elif rand <= 99:

    else:

def enslavedTable539():
    rand = randint(1,20)
    if rand <= 1:
        # Escape
        rand = randint(1,8)
        if rand == 1:
            return 'character escaped slavery, a reward of ' + str(randint(1,10)*100) + ' gold is offered for their capture'
        elif rand == 2:
            return str(randint(1,6)) + ' slaves accompanied the character in their escape from slavery'
        elif rand == 3:
            return 'the government is offering a bounty on the escaped slave'
        elif rand == 4:
            return "the owner's " + random_choice(relativesTable753) + "helped the character escape from slavery"
        elif rand == 5:
            return 'while escaping from slavery, the character killed their owner'
        elif rand == 6:
            return 'while escaping slavery, the character stole ' + giftsTable863()
        elif rand == 7:
            return 'the character, owned by a slaverunner, was set free by the owner who is in love with them'
        elif rand == 8:
            return 're-roll on table shit, ugh.'
    elif rand <= 2:
        #owner decides to free character
        rand = randint(1,10)
        if rand == 1:
            rand = randint(1,8)
            if rand <= 4:
                return 'character is freed from slavery by owner, who is a good friend'
            elif rand <= 7:
                return "character is freed from slavery by owner, who becomes the character's patron" # table 543 here
            elif rand <= 8:
                return "character is freed from slavery by owner, who becomes the character's companion" # table 761 here
        elif rand <= 2:
            return 'character is freed from slavery by owner due to religious conversion, character is paid ' + str(randint(2,20)) + ' gold coins in reparations'
        elif rand <= 4:
            return 'character is reunired with relatives after being freed from slavery'
        elif rand <= 5:
            return 'owner dies and their will specifies that slaves are to be freed'
        elif rand <= 7:
            return ' the slave is unable to be used for work and enlists in the military' #go to table 535
        elif rand <= 8:
            return 'the character escapes slavery with the help of another, who becomes their companion' #go to table 863
        elif rand <= 9:
            return "while in slavery, the character saves their owner's life. the owner gives the character their freedom and " + giftsTable863
        elif rand <= 10:
            return '3x re-roll, will set up later'
    elif rand <= 3:
        return 'the ruler of the land declares slavery illegal and the player is given ' + str(randint(1,100)) + ' gold as reparations'
    elif rand <= 4:
        return 'the character is freed of slavery by saving money and buying their own freedom'
    elif rand <= 5:
        return 'owner dies'
        #there will be a bunch more rolls here
    elif rand <= 7:
        return 'character improves their occupational skill rating by one while in slavery'
    elif rand <= 8:
        return 'character improves their occupational skill rating by ' + str(randint(2,4)) + ' while in slavery'
    elif rand <= 9:
        return 'while in slavery, the character is often beaten by their owner'
    elif rand <= 10:
        return 'character learns an additional skill at rank 1 while enslaved'
    elif rand <= 11:
        return 'as a slave, the character is a sexual plaything of the owner and has no other duties.'
    elif rand <= 12:
        return 'character participates in a slave revolt'
        #more rolls will go here
    elif rand <= 13:
        return 'while enslaved, a character is promoted to a position of authority'
    elif rand <= 14:
        return "while enslaved, the character is the owner's favorite and becomes the senior slave. one of the other slaves becomes the character's rival" #roll table 762 here
    elif rand <= 15:
        return 'character is used as breeding stock. if male, produces ' + str(randint(1,10)) + ' kids per year. if female, one per year'
    elif rand <= 16:
        return 'character is resold ' + str(randint(1,3)) + ' times during their enslavement'
    elif rand <= 17:
        return 'character is branded on their ' + bodyLocationTable867
    elif rand <= 18:
        return 'the character attempts to escape from slavery, fails, and is branded on their ' + bodyLocationTable867 + '. they are also beaten more often'
    elif rand <= 20:
        return 'an exotic event occurs that causes the character to be freed' #roll on table 544 here

def DarksideTraitsTable648():
    rand=randint(2,40)
    if rand == 2:
       return "pessimist"
    elif rand == 3:
        return "egoist"
    elif rand == 4:
        return "obstructive"
    elif rand == 5:
        return "cruel"
    elif rand == 6:
        return "careless"
    elif rand == 7:
        return "thoughtless"
    elif rand == 8:
        return "flippant"
    elif rand == 9:
        return "drunkard"
    elif rand == 10:
        return "suspicious"
    elif rand == 11:
        return "violent"
    elif rand == 12:
        return "argumentative"
    elif rand == 13:
        return "irreverent"
    elif rand == 14:
        return "cheat"
    elif rand == 15:
        return "hateful"
    elif rand == 16:
        return "selfish"
    elif rand == 17:
        return "slovenly"
    elif rand == 18:
        return "filthy"
    elif rand == 19:
        return "tardy"
    elif rand == 20:
        return "self-doubting"
    elif rand == 21:
        return "cowardly"
    elif rand == 22:
        return "disrespectful"
    elif rand == 23:
        return "angry"
    elif rand == 24:
        return "impatient"
    elif rand == 25:
        return "foolish"
    elif rand == 26:
        return "greedy"
    elif rand == 27:
        return "dull"
    elif rand == 28:
        return "vengeful"
    elif rand == 29:
        return "immoral"
    elif rand == 30:
        return "untrustworthy"
    elif rand == 31:
        return "rude"
    elif rand == 32:
        return "harsh"
    elif rand == 33:
        return "unfriendly"
    elif rand == 34:
        return "egotistic"
    elif rand == 35:
        return "lazy"
    elif rand == 36:
        return "liar"
    elif rand == 37:
        return "morose"
    elif rand == 38:
        return "unenthuastic"
    elif rand == 39:
        return "spendthrift"
    elif rand == 40:
        return "tactless"

nonhumansTable751 = {
    'elf': 4,
    'dwarf': 3,
    'halfling': 3,
    'half elf': 4,
    'beastman': 1,
    'reptileman': 1,
    'orc': 1,
    'half orc': 2
}

relativesTable753 = {
    'first cousin': 1,
    'second cousin': 1,
    'distant cousin': 1,
    'son': 1,
    'daughter': 1,
    'sister': 1,
    'brother': 1,
    'spouse': 1,
    'aunt': 1,
    'uncle': 1,
    'great aunt': 1,
    'great uncle': 1,
    'mother': 1,
    'father': 1,
    'grandmother': 1,
    'grandfather': 1,
    'great grandmother': 1,
    'great grandfather': 1,
    'descendent': 1,
    'unknown relation': 1
}

def guardiansTable754(cuMod):
    rand = randint(1,20)
    if rand <= 5:
        return random_choice(relativesTable753)
    elif rand <= 8:
        return 'raised in an orphanage'
    elif rand <= 10:
        global charAdopted
        charAdopted = True
        familyTable106a(cuMod)
    elif rand <= 11:
        return 'raised by priests or monks of ' + deitiesTable864(cuMod)
    elif rand <= 12:
        return 'raised by ' + random_choice(nonhumansTable751)
    elif rand <= 13:
        return 'sold into slavery ' + enslavedTable539()
    elif rand <= 14:
        return 'raised on the street by beggars and prostitutes'
    elif rand <= 15:
        return "raised by a thieves' guild" #table534 here
    elif rand <= 16:
        return 'raised by different relatives, passed between them until coming of age'
    elif rand <= 17:
        return 'raised by an adventurer: ' #table757
    elif rand <= 18:
        return 'character mysteriously disappeared for ' + str(randint(1,10)) + ' years'
    elif rand <= 19:
        return 'raised by beasts in the wild'
    elif rand <= 20:
        return 'raised by ' #table 756

criminalTable755 = {
    'murderer': 1,
    'kidnapper': 2,
    'thief': 3,
    'pickpocket': 4,
    'extortionist': 5,
    'con man': 6,
    'armed robber': 7,
    'highwayman': 8,
    'gang bandit': 9,
    'professional assassin': 10,
    'drug dealer': 11,
    'mugger': 12,
    'horse thief': 13,
    'rustler': 14,
    'thug': 15,
    'pimp': 16,
    'prostitute': 17,
    'gang leader': 18,
    'rapist': 19,
    'pirate': 20
}

nobleTable758prim = {
    'high king': 1,
    'chieftain': 29,
    'subchieftain': 70
}

nobleTable758nomad = {
    'kahn': 10,
    'chieftain': 30,
    'subchieftain': 40,
    'hetman': 20
}

nobleTable758barb = {
    'high king': 2,
    'king': 13,
    'prince(ss)': 10,
    'chieftain': 20,
    'jarl': 15,
    'subchieftain': 10,
    'baron': 5,
    'prince(ss) (royal)': 5,
    'hetman': 20
}

nobleTable758civil = {
    'emperor': 1,
    'king': 4,
    'prince(ss) (royal)': 10,
    'archduke': 5,
    'duke': 5,
    'marquis': 10,
    'viscount': 15,
    'count': 10,
    'baron': 15,
    'lord': 3,
    'prince(ss)': 12,
    'knight': 10
}

def nobleTable758tiMod(nobleTitle):
    if nobleTitle == 'hetman':
        return randint(1,6)
    elif nobleTitle == 'knight':
        return randint(2,12)
    elif nobleTitle == 'prince(ss)':
        return randint(4,40)
    elif nobleTitle == 'lord':
        return randint(2,16)
    elif nobleTitle == 'baron':
        return randint(2,20)
    elif nobleTitle == 'count':
        return randint(3,18)
    elif nobleTitle == 'subchieftain':
        return randint(2,12)
    elif nobleTitle == 'jarl':
        return randint(3,18)
    elif nobleTitle == 'viscount':
        return randint(3,24)
    elif nobleTitle == 'chieftain':
        return randint(3,18)
    elif nobleTitle == 'marquis':
        return randint(3,30)
    elif nobleTitle == 'duke':
        return randint(4,32)
    elif nobleTitle == 'archduke':
        return randint(4,40)
    elif nobleTitle == 'prince(ss) (royal)':
        return randint(4,40)
    elif nobleTitle == 'kahn':
        return randint(5,40)
    elif nobleTitle == 'king':
        return 39
    elif nobleTitle == 'high king':
        return randint(5,50)
    elif nobleTitle == 'emperor':
        return 60
    else:
        raise ValueError("\nnobleTable758tiMod isn't getting a nobleTitle pushed to it.")

def unusualPetsTable759():
    rand = randint(1,20)
    if rand <= 2:
        petType = 'dog'
    elif rand <= 4:
        petType = 'cat'
    elif rand <= 5:
        petType = 'rabbit'
    elif rand <= 6:
        petType = 'lizard'
    elif rand <= 7:
        petType = 'monkey'
    elif rand <= 8:
        petType = 'raccoon'
    elif rand <= 9:
        petType = 'rat'
    elif rand <= 10:
        petType = 'snake'
    elif rand <= 11:
        petType = 'hawk'
    elif rand <= 12:
        petType = 'mouse'
    elif rand <= 13:
        petType = 'ferret'
    elif rand <= 14:
        petType = 'songbird'
    elif rand <= 15:
        rand = randint(1,3)
        if rand == 3:
            petType = 'fish (that can survive out of water)'
        else:
            petType = 'fish'
    elif rand <= 16:
        petType = 'puppy'
    elif rand <= 17:
        petType = 'mini-dragon'
    elif rand <= 18:
        petType = 'big cat'
    elif rand <= 19:
        petType = 'baby bear that stays a baby'
    elif rand <= 20:
        petType = 'something alien'
    petAbility = specialPetAbilitiesTable760()
    return petType + ' (' + petAbility + ')'

def specialPetAbilitiesTable760():
    rand = randint(1,20)
    if rand <= 1:
        return 'has wings'
    elif rand <= 2:
        return 'very intelligent'
    elif rand <= 3:
        return 'telepathic'
    elif rand <= 4:
        return 'unusual color: ' + colorsTable865
    elif rand <= 5:
        rand = randint(1,10)
        return 'pet is made of odd substance'
    elif rand <= 6:
        return 'pet has physical affliction ' #table874 here
    elif rand <= 7:
        return 'pet can use magic spells'
    elif rand <= 8:
        return 'pet is invisible to all but owner'
    elif rand <= 9:
        return 'pet regenerates damage done to it'
    elif rand <= 10:
        return 'when killed, pet will possess nearest animal'
    elif rand <= 11:
        rand = randint(1,2)
        if rand == 1:
            return 'pet is unusually large'
        else:
            return 'pet is unusually small'
    elif rand <= 12:
        return 'once per day, pet may assume attractive human form for ' + str(randint(1,6)) + ' hours'
    elif rand <= 13:
        return 'draws magical power from its master'
    elif rand <= 14:
        return 'supplies magical power to master'
    elif rand <= 15:
        return "pet's life is added to character's own as long as the pet lives"
    elif rand <= 16:
        return 'breathes fire'
    elif rand <= 17:
        return 'can increase its size and strength ' + str(randint(1,10)) + ' times their normal amount once per day for ' + str(randint(1,6)) + ' hours'
    elif rand <= 18:
        return 'can provide master with ' + str(randint(1,6)) + ' gold per day'
    elif rand <= 19:
        return 'can turn into mist at will'
    elif rand <= 20:
        return 'reroll shit'

def companionTable761():
    companionWho = companionTable761a()
    companionWhy = companionTable761b()
    companionPersonality = companionTable761c()
    return companionWho + ', because ' + companionWhy + ', personality: ' + companionPersonality

def companionTable761a():
    rand = randint(1,9) #easily able to add 10 to this for the re-roll once everything is set up
    if rand == 1:
        return 'childhood friend'
    elif rand == 2:
        return 'a family member, ' + random_choice(relativesTable753)
    elif rand == 3:
        return 'a nonhuman, ' + random_choice(nonhumansTable751)
    elif rand == 4:
        return 'a stranger, ' #table 750 go hurr
    elif rand == 5:
        return 'an intelligent, articulate inanimate object'
    elif rand == 6:
        return 'a kid aged ' + str(randint(7,13))
    elif rand == 7:
        rand = randint(1,2)
        if rand == 1:
            return 'an older sibling'
        else:
            return 'a younger sibling'
    elif rand == 8:
        return 'an adventurer, ' #table 757
    elif rand == 9:
        return 'a former enemy or rival, ' #table 762 go hurr
    #elif rand == 10:

def companionTable761b():
    rand = randint(1,9)
    if rand == 1:
        return 'character saved their life'
    elif rand == 2:
        return 'they seek a similar goal, are friendly rivals'
    elif rand == 3:
        return 'parents were companions in adventure'
    elif rand == 4:
        return 'they share the same enemy'
    elif rand == 5:
        return 'they were in the same place and in trouble at the same time'
    elif rand == 6:
        return 'the companion imagines the character a hero and wants to learn from them'
    elif rand == 7:
        return "the companion's original intent was to steal from the character"
    elif rand == 8:
        return 'companion feels a need to protect the character'
    elif rand == 9:
        return 'mysterious voices and feelings told the companion to seek out the character and join them'

def companionTable761c():
    rand = randint(1,10)
    if rand <= 3:
        return 'loyal friend'
    elif rand <= 5:
        return 'bumbling buffoon'
    elif rand <= 6:
        return 'grim, quiet ally'
    elif rand <= 7:
        return 'enthusiastic leader-type'
    elif rand <= 8:
        return 'a wise-cracking smart mouth who complains'
    elif rand <= 9:
        return 'rowdy fighter'
    elif rand <= 10:
        return 'incurable romantic'

def giftsTable863():
    rand = randint(1,20)
    if rand <= 1:
        return random_choice(giftsTable863a)
    elif rand <= 2:
        return 'guardianship of a young ward. Use table 761'
    elif rand <= 3:
        return 'unusual pet. Use table 760'
    elif rand <= 4:
        return random_choice(giftsTable863b)
    elif rand <= 5:
        return 'a tapestry'
    elif rand <= 6:
        return 'an anachronistic device'
    elif rand <= 7:
        return 'a key'
    elif rand <= 8:
        return 'a locked or sealed book'
    elif rand <= 9:
        return 'a shield'
    elif rand <= 10:
        return 'a sealed bottle'
    elif rand <= 11:
        return 'a tarnished old helmet'
    elif rand <= 12:
        return 'a bound wooden staff'
    elif rand <= 13:
        return 'a riding animal'
    elif rand <= 14:
        return 'a deed to ' + random_choice(giftsTable863c)
    elif rand <= 15:
        return 'a musical instrument'
    elif rand <= 16:
        return random_choice(giftsTable863d)
    elif rand <= 17:
        return 'a pouch of papers containing ' + random_choice(giftsTable863e)
    elif rand <= 18:
        return 'a sealed trunk'
    elif rand <= 19:
        return 'a chainmail hauberk'
    elif rand <= 20:
        return 'roll again shenanigans'

giftsTable863a = {
    'an ornate dagger': 1,
    'an ornate sword': 1,
    'a plain sword': 1,
    'a mace': 1,
    'an ornate spear': 1,
    'a well-made bow': 1,
    'an ornate battle axe': 1,
    'an exotic weapon': 1,
}

giftsTable863b = {
    'amulet': 1,
    'necklace': 1,
    'earrings': 1,
    'tiara': 1,
    'torc': 1,
    'arm band': 1,
    'ring': 1,
    'pin or brooch': 1,
}

giftsTable863c = {
    'a tract of land': 1,
    'an ancient castle': 1,
    'a country manor': 1,
    'an elegant town house': 1,
    'a temple': 1,
    'a factory': 1,
    'ancient ruins': 1,
    'an inn': 1,
    'an apartment building': 1,
}

giftsTable863d = {
    'a hat': 1,
    'a pair of shoes': 1,
    'a belt': 1,
    'a cape': 1,
    'a tunic': 1,
    'trousers': 1,
    'a pair of stockings': 1
}

giftsTable863e = {
    "an ancient ancestor's letter to his descendents": 1,
    'a map': 1,
    'an undelivered letter': 1,
    'diagrams and plans for a mysterious invention': 1,
    'a scroll of magic spells': 1,
    'a wild story of adventure': 1,
    'a last will and testament determining that the character is an heir': 1,
    'a treasure map': 1,
    "the character's true family history": 1
}

def deitiesTable864(cuMod=0):
    rand = randint(1,20) + cuMod
    if rand <= 1:
        return 'ancestor worship'
    elif rand <= 2:
        return 'beast gods'
    elif rand <= 3:
        return 'hunting god'
    elif rand <= 4:
        return 'trickster'
    elif rand <= 5:
        return 'earth goddess'
    elif rand <= 6:
        return 'agricultural goddess'
    elif rand <= 8:
        return 'agricultural goddess'
    elif rand <= 10:
        return 'ruling deity'
    elif rand <= 11:
        return 'sea god'
    elif rand <= 12:
        return 'sun god'
    elif rand <= 13:
        return 'moon goddess'
    elif rand <= 14:
        return 'storm god'
    elif rand <= 15:
        return 'evil god'
    elif rand <= 16:
        return 'war god'
    elif rand <= 17:
        return 'love goddess'
    elif rand <= 18:
        return 'underworld god'
    elif rand <= 19:
        return 'god of wisdom'
    elif rand <= 20:
        return 'healing god'
    elif rand <= 21:
        return 'trade god'
    elif rand <= 22:
        return 'luck goddess'
    elif rand <= 23:
        return 'night goddess'
    elif rand <= 24:
        return 'god of thieves'
    elif rand <= 27:
        return 'decadent god'
    else:
        raise ValueError("I done fucked up on the deitiesTable864")

colorsTable865 = {
    'red': 1,
    'red orange': 1,
    'orange': 1,
    'yellow orange': 1,
    'yellow': 1,
    'yellow-green': 1,
    'green': 1,
    'blue-green': 1,
    'blue': 1,
    'blue-violet': 1,
    'violet': 1,
    'red violet': 1,
    'pink': 1,
    'white': 1,
    'black': 1,
    'gray': 1,
    'maroon': 1,
    'silver': 1,
    'gold': 1,
    'reroll': 1
}

birthmarksTable866 = {
    'dragon': 1,
    'skull': 1,
    'bat': 1,
    'sword': 1,
    'hand': 1,
    'crescent moon': 1,
    'claw': 1,
    'eagle': 1,
    'fish': 1,
    'animal (you decide)': 1
}

bodyLocationTable867 = {
    'right foot': 1,
    'left foot': 1,
    'right leg': 1,
    'left leg': 1,
    'abdomen': 2,
    'buttocks': 2,
    'back': 1,
    'chest': 4,
    'right arm': 1,
    'left arm': 1,
    'right hand': 1,
    'left hand': 1,
    'head': 1,
    'face': 2
}

'''
This is an easy copy/paste for creating dicts:
Table = {
    '': ,
    '': ,
    '': ,
    '': ,
    '': ,
    '': ,
    '': ,
    '':
}
'''
