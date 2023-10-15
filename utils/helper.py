from . import constants
import random
from utils.models import Color, Shape, Shading, Number, Card, Table


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


def get_cards(number_of_cards):
    if number_of_cards > 82:
        return ValueError
    random_cards = set()
    while len(random_cards) < number_of_cards:
        card = get_random_card()
        random_cards.add(card)

    return random_cards
