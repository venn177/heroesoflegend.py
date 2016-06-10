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
