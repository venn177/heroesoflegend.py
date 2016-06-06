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

birthTable104 = {

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
