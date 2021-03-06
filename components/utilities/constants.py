"""This file contains the various necessary constants for the game."""

import tcod
from enum import auto, Enum

DIRECTIONS = {
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
    "UP": (0, -1),
    "DOWN": (0, 1)
}

COLOURS = {
    "RED": tcod.red,
    "WHITE": tcod.white,
    "GREY": tcod.grey,
    "YELLOW": tcod.yellow,
    "GOLD": tcod.gold,
    "BROWN": tcod.brass,
    "BLACK": tcod.black,
    "GREEN": tcod.green,
    "PURPLE": tcod.purple,
    "PATH": (179, 102, 255),
    "RADIUS": (140, 26, 255),
    "TARGET": (102, 0, 204),
    "TEMP": tcod.chartreuse
}


class RenderOrder(Enum):
    FEATURE = auto()
    ITEM = auto()
    ENTITY = auto()
