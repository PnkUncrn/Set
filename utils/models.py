# change to pydantic
from enum import Enum
from . import constants
from itertools import combinations as combinations
import random


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
    def __init__(self, number_of_cards=12, cards_provided=None):
        self.number_of_cards = number_of_cards
        self.cards = get_cards(self.number_of_cards, cards_provided)

    # list of cards given, return a list of sets
    # sets must be unique = set of tuples?
    def get_sets(self):
        sets_found = set()
        card_combination_iter = combinations(self.cards, 2)
        for card_combo in card_combination_iter:
            created_card = create_third_card(card_combo[0], card_combo[1])
            if created_card in self.cards:
                sets_found.add(frozenset({card_combo[0], card_combo[1], created_card}))

        sets_found_list = [list(x) for x in sets_found]

        return sets_found_list

    def __str__(self):
        print("The Table with {} cards:".format(self.number_of_cards))
        for card in self.cards:
            print(card)
        return f'End Table'


# given three cards, verify its a set
def is_it_set(card1, card2, card3):
    created_card = create_third_card(card1, card2)
    return card3 == created_card


# given 2 cards, generate the third such that the three cards are a set
def create_third_card(card1, card2):
    created_card = Card()
    meta_attr = get_meta_attr(card1, card2)
    if meta_attr[constants.COLOR] is constants.SAME:
        created_card.color = card1.color
    else:
        card_color_list = [card1.color, card2.color]
        leftover_color = [c for c in Color if c not in card_color_list]
        created_card.color = leftover_color[0]

    if meta_attr[constants.SHAPE] is constants.SAME:
        created_card.shape = card1.shape
    else:
        card_shape_list = [card1.shape, card2.shape]
        leftover_shape = [s for s in Shape if s not in card_shape_list]
        created_card.shape = leftover_shape[0]

    if meta_attr[constants.NUMBER] is constants.SAME:
        created_card.number = card1.number
    else:
        card_number_list = [card1.number, card2.number]
        leftover_number = [n for n in Number if n not in card_number_list]
        created_card.number = leftover_number[0]

    if meta_attr[constants.SHADING] is constants.SAME:
        created_card.shading = card1.shading
    else:
        card_shading_list = [card1.shading, card2.shading]
        leftover_shading = [s for s in Shading if s not in card_shading_list]
        created_card.shading = leftover_shading[0]
    return created_card


# given 2 card, greb their meta attributes
def get_meta_attr(card1: Card, card2: Card):
    meta_attr = {constants.COLOR: compare_attributes(card1.color, card2.color),
                 constants.SHAPE: compare_attributes(card1.shape, card2.shape),
                 constants.SHADING: compare_attributes(card1.shading, card2.shading),
                 constants.NUMBER: compare_attributes(card1.number, card2.number)}

    return meta_attr


# given 2 attributes return if they are the same of different
def compare_attributes(attribute1, attribute2):
    if attribute1 == attribute2:
        return constants.SAME
    else:
        return constants.DIFFERENT


# given a list of cards, find list of sets.
# sets shouldnt be repeated
# generate a list of sets, each card is unique
def get_random_card():
    random_card = Card()
    random_card.color = random.choice(list(Color))
    random_card.shape = random.choice(list(Shape))
    random_card.shading = random.choice(list(Shading))
    random_card.number = random.choice(list(Number))

    return random_card


def get_cards(total_cards, cards_provided):
    if total_cards > 82:
        raise ValueError

    cards_set = set()
    cards_to_be_generated = total_cards
    if cards_provided:
        if len(cards_provided) > total_cards:
            raise ValueError
        cards_to_be_generated = cards_to_be_generated - len(cards_provided)
        for card in cards_provided:
            cards_set.add(card)

    while len(cards_set) < total_cards:
        card = get_random_card()
        cards_set.add(card)

    return cards_set
