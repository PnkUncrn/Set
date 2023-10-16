from enum import Enum
import random
from itertools import combinations as combinations
import utils.constants as constants
from utils.models import Color, Shape, Shading, Number, Table, Card
import utils


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
# card1 = Card(color=Color.red, shape=Shape.oval, shading=Shading.striped, number=Number.one, position=None)
# card2 = Card(color=Color.green, shape=Shape.oval, shading=Shading.striped, number=Number.one, position=None)
# card3 = Card(color=Color.purple, shape=Shape.oval, shading=Shading.striped, number=Number.one, position=None)
#
# cards = get_cards(50)
# print(cards)
# num = 1

# card = get_random_card()
# print(card)

card2 = Card(color=Color.green, shape=Shape.oval, shading=Shading.striped, number=Number.one, position=None)
card3 = Card(color=Color.purple, shape=Shape.oval, shading=Shading.striped, number=Number.one, position=None)
table = Table(3, [card2, card3])
print(table)
a = table.get_sets()
for ind, val in enumerate(a):
    print("The set {}".format(ind+1))
    for card in val:
        print(card)

# print("Length of cards", len(cards))
# for card in cards:
#     print("Card {} ", num)
#     num = num+1
#     card.print_card()
