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
    'human': 14,
    'elf': 2,
    'dwarf': 1,
    'halfling': 1,
    'half elf': 1,
    'other races': 1
}

raceTable101a = {
    'beastman': 3,
    'reptileman': 2,
    'orc': 1,
    'half orc': 4
}

cultureTable102 = {
    'primitive': 1,
    'nomad': 2,
    'barbarian': 3,
    'civilized': 3,
    'civilized-decadent': 1
}

def cultureTable102a(culture):
    if culture == 'primitive':
        return(-3)
    elif culture == 'nomad':
        return(0)
    elif culture == 'barbarian':
        return(2)
    elif culture == 'civilized':
        return(4)
    elif culture == 'civilized-decadent':
        return(7)

def socialTable103(cuMod, tiMod, charCulture):
    rand = randint(1,100) + cuMod + tiMod
    if rand <= 12:
        return('destitute', -3, '', 0)
    elif rand <= 40:
        return('poor', -1, '', 0)
    elif rand <=84:
        return('comfortable', 0, '', 0)
    elif rand == 85:
        socialTable103(0, tiMod, charCulture)
    elif rand <= 96:
        return('well-to-do', 2, '', 0)
    elif rand <= 98:
        rand = randint(1,100)
        if rand <= tiMod + 1:
            return('extremely wealthy', 8, '', 0)
        else:
            return('wealthy', 4, '', 0)
    elif rand >= 99:
        if charCulture == 'primitive':
            nobleTitle = random_choice(nobleTable758prim)
        elif charCulture == 'nomad':
            nobleTitle = random_choice(nobleTable758nomad)
        elif charCulture == 'barbarian':
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
        return('destitute', -3, nobleTitle, tiMod)
    elif rand <= 40:
        return('poor', -1, nobleTitle, tiMod)
    elif rand <=84:
        return('comfortable', 0, nobleTitle, tiMod)
    elif rand == 85:
        return socialTable103a(0, tiMod, charCulture, nobleTitle)
    elif rand <= 96:
        return('well-to-do', 2, nobleTitle, tiMod)
    elif rand <= 98:
        rand = randint(1,100)
        if rand <= tiMod + 1:
            return('extremely wealthy', 8, nobleTitle, tiMod)
        else:
            return('wealthy', 4, nobleTitle, tiMod)
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
        rand = randint(1,20)
        if rand <= 8:
            return guardiansTable754(cuMod)
        else:
            global charAdopted
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

relativesTable753 = {
    'first cousin': 1,
    'second cousin': 2,
    'distant cousin': 3,
    'son': 4,
    'daughter': 5,
    'sister': 6,
    'brother': 7,
    'spouse': 8,
    'aunt': 9,
    'uncle': 10,
    'great aunt': 11,
    'great uncle': 12,
    'mother': 13,
    'father': 14,
    'grandmother': 15,
    'grandfather': 16,
    'great grandmother': 17,
    'great grandfather': 18,
    'descendent': 19,
    'unknown relation': 20
}

def guardiansTable754(cuMod):
    rand = randint(1,20)
    if rand <= 5:
        return random_choice(relativesTable753)
    if rand <= 8:
        return 'raised in an orphanage'
    if rand <= 10:
        global charAdopted
        charAdopted = True
        familyTable106a(cuMod)
    if rand <= 11:
        return 'raised by priests or monks of ' + deitiesTable864(cuMod)
    if rand <= 12:
        return 'raised by ' + random_choice(nonhumansTable751)
    if rand <= 13:
        #
    if rand <= 14:
        #
    if rand <= 15:
        #
    if rand <= 16:
        #
    if rand <= 17:
        #
    if rand <= 18:
        #
    if rand <= 19:
        #
    if rand <= 20:
        #

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
            #re-roll on table shit, ugh.
    elif rand <= 2:

    elif rand <= :

    elif rand <= :

    elif rand <= :

    elif rand <= :

    elif rand <= :

    elif rand <= :

    elif rand <= :

    elif rand <= :

    elif rand <= :

    elif rand <= :

    elif rand <= :


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
    'prince': 10,
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

def giftsTable863():
    rand = randint(1,20)
    if rand <= 1:
        return random_choice(giftsTable863a)
    elif rand <= 2:
        #guardianship of a young ward. Use table 761
    elif rand <= 3:
        #unusual pet. Use table 760
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
        #roll again shenanigans

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

def deitiesTable864(cuMod):
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
