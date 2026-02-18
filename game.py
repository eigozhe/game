# создать разные типы оружия и сделать возможность менять их вне боя (во время боя их переключать нелья а если хочется то тратиться действие) также чтобы характеристики оружия либо менялись в статах персонажа или (по возможности) подключать их отдельно в качестве отдельного масива
from random import randint

steve = {'atack':10,'strongAtack':25,'stamina':100,'rest':20,'hp':100,'chanceAtack':(40,80),'missAtack':(0,39),'chanceSuperatack':(81,100)}

creaper= {'atack':12,'hp':150,'chanceAtack':(40,100),'missAtack':(0,39),'chanceSuperatack':(101,101)}

def inventoryy():
    return {
        'ironSword':10,
        'battleAxe':15,
        'assassinDagger':20,
        'longbow':25
    }

inventory = inventoryy()
steve['equippedWeapon'] = 'ironSword'

def attack(atack, target):
    target = target - atack
    print(target)

attack(steve['atack'], creaper['hp'])
attack(creaper['atack'], steve['hp'])


def staminaa(stamina, target):
    stamina = stamina - target
    print(stamina)

attack(steve['atack'], steve['stamina'])
attack(steve['strongAtack'], steve['stamina'])


def chance(chanceAtack, missAtack, chanceSuperatack):
    chancee = randint(1, 100)
    print(chancee)

    return ["miss", "attack", "strongAttack"][
        (chancee >= chanceAtack[0]) +
        (chancee >= chanceSuperatack[0])
    ]

result = chance(
    steve['chanceAtack'],
    steve['missAtack'],
    steve['chanceSuperatack']
)
print(result)

result = chance(
    creaper['chanceAtack'],
    creaper['missAtack'],
    creaper['chanceSuperatack']
)
print(result)

while steve['hp'] > 0 and creaper['hp'] > 0:

    print(f"""
____________________________________________________________
| steve {steve['hp']} | Enemy {creaper['hp']}        |
| stamina {steve['stamina']} | EnemyDamage {creaper['atack']} |
| weapon {steve['equippedWeapon']}|
------------------------------------------------------------
| 1. attack                                              |
| 2. time (+20 stamina)                                  |
| 3. strong attack                                       |
| 4. change weapon                                       |
____________________________________________________________
""")

    game = int(input("what you wanna do: "))

