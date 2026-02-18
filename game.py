# создать разные типы оружия и сделать возможность менять их вне боя (во время боя их переключать нелья а если хочется то тратиться действие) также чтобы характеристики оружия либо менялись в статах персонажа или (по возможности) подключать их отдельно в качестве отдельного масива
from random import randint

steve = {'atack': 10,'strongAtack': 25,'stamina': 100,'rest': 20,'hp': 100,'chanceAtack': (40, 80),'missAtack': (0, 39),'chanceSuperatack': (81, 100),'weapon': 'ironSword'}

creaper = {'atack': 12,'hp': 150,'chanceAtack': (61, 100),'missAtack': (0, 60),'chanceSuperatack': (101, 101)}

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


def attack(atack, target):
    target = target - atack
    print("target hp:", target)
    return target


def staminaa(stamina, cost):
    stamina = stamina - cost
    print("stamina:", stamina)
    return stamina


def chance(chanceAtack, missAtack, chanceSuperatack):
    chancee = randint(1, 100)
    print("randint:", chancee)
    return ["miss", "attack", "strongAttack"][
        (chancee >= chanceAtack[0]) + (chancee >= chanceSuperatack[0])
    ]


while steve['hp'] > 0 and creaper['hp'] > 0:

    print("1 - attack")
    print("2 - strong attack")
    print("3 - rest")
    print("4 - inventory")

    game = int(input("what you wanna do: "))
