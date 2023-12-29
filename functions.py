import random

cards = {
    'ace': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'queen': 10,
    'jack': 10,
    'king': 10
}


def draw_card():
    card = random.choice(list(cards.values()))
    return card
