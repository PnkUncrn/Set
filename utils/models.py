# change to pydantic
from enum import Enum
from . import constants
from itertools import combinations as combinations
from . import helper


class Color(str, Enum):
    green = constants.GREEN
    purple = constants.PURPLE
    red = constants.RED


class Shape(str, Enum):
    oval = constants.OVAL
    diamond = constants.DIAMOND
    squiggle = constants.SQUIGGLE


class Shading(str, Enum):
    striped = constants.STRIPED
    solid = constants.SOLID
    open = constants.OPEN


class Number(Enum):
    one = 1
    two = 2
    three = 3


class Card:
    def __init__(self, color=None, shape=None, shading=None, number=None, position=None):
        self.color = color
        self.shape = shape
        self.shading = shading
        self.number = number
        self.position = position

    def __key(self):
        return self.color, self.shape, self.shading, self.number

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.__key() == other.__key()
        return NotImplemented

    def __str__(self):
        return f'The card has following properties:\n Color: {self.color} \n Shape: {self.shape} \n ' \
               f'Shading: {self.shading} \n Number: {self.number} \n '


class Table:
    def __init__(self, number_of_cards=12):
        self.number_of_cards = number_of_cards
        self.cards = helper.get_cards(self.number_of_cards)

    # list of cards given, return a list of sets
    # sets must be unique = set of tuples?
    def get_sets(self):
        sets_found = set()
        card_combination_iter = combinations(self.cards, 2)
        for card_combo in card_combination_iter:
            created_card = helper.create_third_card(card_combo[0], card_combo[1])
            if created_card in self.cards:
                sets_found.add(frozenset({card_combo[0], card_combo[1], created_card}))

        sets_found_list = [list(x) for x in sets_found]

        return sets_found_list

    def __str__(self):
        print("The Table with {} cards:".format(self.number_of_cards))
        for card in self.cards:
            print(card)
        return f'End Table'
