from enum import Enum
import random

SAME = 'same'
DIFFERENT = 'different'
COLOR = 'color'
SHAPE = 'shape'
SHADING = 'shading'
NUMBER = 'number'
GREEN = 'green'
PURPLE = 'purple'
RED = 'red'
OVAL = 'oval'
DIAMOND = 'diamond'
SQUIGGLE = 'squiggle'
STRIPED = 'striped'
SOLID = 'solid'
OPEN = 'open'


# change to pydanticc
class Color(str, Enum):
    green = GREEN
    purple = PURPLE
    red = RED


class Shape(str, Enum):
    oval = OVAL
    diamond = DIAMOND
    squiggle = SQUIGGLE


class Shading(str, Enum):
    striped = STRIPED
    solid = SOLID
    open = OPEN


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

    def print_card(self):
        print(
            "The card has following properties:\n Color: {0} \n Shape: {1} \n Shading: {2} \n Number: {3} \n "
            "Position: {4} ".format(self.color, self.shape, self.shading, self.number, self.position))


# given three cards, verify its a set
def is_it_set(card1, card2, card3):
    created_card = create_third_card(card1, card2)
    return card3 == created_card


# given 2 cards, generate the third such that the three cards are a set
def create_third_card(card1, card2):
    created_card = Card()
    meta_attr = get_meta_attr(card1, card2)
    if meta_attr[COLOR] is SAME:
        created_card.color = card1.color
    else:
        card_color_list = [card1.color, card2.color]
        leftover_color = [c for c in Color if c not in card_color_list]
        created_card.color = leftover_color[0]
    if meta_attr[SHAPE] is SAME:
        created_card.shape = card1.shape
    else:
        card_shape_list = [card1.shape, card2.shape]
        leftover_shape = [s for s in Shape if s not in card_shape_list]
        created_card.shape = leftover_shape[0]
    if meta_attr[NUMBER] is SAME:
        created_card.number = card1.number
    else:
        card_number_list = [card1.number, card2.number]
        leftover_number = [n for n in Number if n not in card_number_list]
        created_card.number = leftover_number[0]
    if meta_attr[SHADING] is SAME:
        created_card.shading = card1.shading
    else:
        card_shading_list = [card1.shading, card2.shading]
        leftover_shading = [s for s in Shading if s not in card_shading_list]
        created_card.shading = leftover_shading[0]
    return created_card


# given 2 card, greb their meta attributes
def get_meta_attr(card1: Card, card2: Card):
    meta_attr = {COLOR: compare_attributes(card1.color, card2.color),
                 SHAPE: compare_attributes(card1.shape, card2.shape),
                 SHADING: compare_attributes(card1.shading, card2.shading),
                 NUMBER: compare_attributes(card1.number, card2.number)}

    return meta_attr


# given 2 attributes return if they are the same of different
def compare_attributes(attribute1, attribute2):
    if attribute1 == attribute2:
        return SAME
    else:
        return DIFFERENT


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


def get_cards(number_of_cards):
    if number_of_cards > 82:
        return ValueError
    random_cards = set()
    while len(random_cards) < number_of_cards:
        card = get_random_card()
        random_cards.add(card)

    return random_cards


class Table:
    def __init__(self, number_of_cards):
        self.number_of_cards = number_of_cards
        self.cards = get_cards(self.number_of_cards)

    #list of cards given, return a list of sets
    #sets must be unique = set of tuples?
    def get_sets(self):
        card_list = list(self.cards)
        #user iter tools to generate combinations



# card1 = Card(color=Color.red, shape=Shape.oval, shading=Shading.striped, number=Number.one, position=None)
# card2 = Card(color=Color.purple, shape=Shape.oval, shading=Shading.solid, number=Number.two, position=None)
# card3 = Card(color=Color.green, shape=Shape.oval, shading=Shading.open, number=Number.one, position=None)
#
# card1.print_card()
# card2.print_card()
# card3.print_card()
#
# generated_card = create_third_card(card1, card2)
#
# result = is_it_set(card1, card2, card3)
# print(result)

# set_of_cards = get_cards(5)
#
# num = 0
# for card in set_of_cards:
#     num = num+1
#     print("Card {} in set".format(num))
#     card.print_card()

# can two same cards be in set
card1 = Card(color=Color.red, shape=Shape.oval, shading=Shading.striped, number=Number.one, position=None)
card2 = Card(color=Color.green, shape=Shape.oval, shading=Shading.striped, number=Number.one, position=None)
card3 = Card(color=Color.purple, shape=Shape.oval, shading=Shading.striped, number=Number.one, position=None)

cards = get_cards(500)
print(cards)
num = 1
# print("Length of cards", len(cards))
# for card in cards:
#     print("Card {} ", num)
#     num = num+1
#     card.print_card()
