# change to pydantic
from enum import Enum
from . import constants


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
