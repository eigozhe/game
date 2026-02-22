# создать разные типы оружия и сделать возможность менять их вне боя (во время боя их переключать нелья а если хочется то тратиться действие) также чтобы характеристики оружия либо менялись в статах персонажа или (по возможности) подключать их отдельно в качестве отдельного масива
from random import randint

steve = {
    'name': 'steve',
    'atack': 10,
    'strongAtack': 25,
    'stamina': 100,
    'rest': 20,
    'hp': 100,
    'weapon': 'ironSword',
    'chanceAtack': (40, 80),
    'missAtack': (0, 39),
    'chanceSuperatack': (81, 100)
}

creaper = {
    'name': 'creaper',
    'atack': 12,
    'hp': 150,
    'chanceAtack': (61, 100),
    'missAtack': (0, 60),
    'chanceSuperatack': (101, 101)
}

inventory = {
    1: ('ironSword', 10),
    2: ('battleAxe', 15),
    3: ('assassinDagger', 20),
    4: ('longbow', 25)
}

def Inventory(choice, steve):
    if choice in inventory:
        steve['weapon'], steve['atack'] = inventory[choice]
        print("You equipped", steve['weapon'])
    else:
        print("Wrong choice")
        
        
def chance(chanceAtack, missAtack, chanceSuperatack):
    chancee = randint(1, 100)
    print("randint:", chancee)
    return ["miss", "attack", "strongAttack"][
        (chancee >= chanceAtack[0]) + (chancee >= chanceSuperatack[0])
    ]

def attack(atack, defender):
    defender['hp'] -= atack
    print(defender['name'], "hp:", defender['hp'])

def staminaa(stamina, rest):
    stamina = stamina + rest
    print("stamina:", stamina)
    return stamina


def show_table(steve, creaper):
    print(f'''_____________________________________________________________________
    | Steve {steve['hp']:<5}                               | Creaper {creaper['hp']:<5}  
    | stamina {steve['stamina']:<5}                        | EnemyDamage {creaper['atack']:<5} 
    | 1. attack (cost 10) - {steve['atack']:<5}            |                             
    | 2. Time (+{steve['rest']} stamina)                   |                             
    | 3. strong attack (cost 35) - {steve['strongAtack']:<5}|                            
    | 4. inventory                                         |                             
    _____________________________________________________________________________
    ''')

while steve['hp'] > 0 and creaper['hp'] > 0:

    show_table(steve, creaper)

    game = int(input("what you wanna do: "))

    # ----- STEVE TURN -----
    if game == 1:
        attack(steve['atack'], creaper)

    elif game == 2:
        attack(steve['strongAtack'], creaper)

    elif game == 3:
        steve['stamina'] = staminaa(steve['stamina'], steve['rest'])

    elif game == 4:
        print("1 - ironSword")
        print("2 - battleAxe")
        print("3 - assassinDagger")
        print("4 - longbow")

        choice = int(input("Choose weapon: "))
        Inventory(choice, steve)

    else:
        print("Wrong action")

    # ----- IF CREAPER DEAD -----
    if creaper['hp'] <= 0:
        break

    # ----- CREAPER TURN -----
    print("\ncreaper turn!")
    attack(creaper['atack'], steve)

# ----- END GAME -----
if steve['hp'] <= 0:
    print("You lose")
else:
    print("You win")
