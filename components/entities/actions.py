"""
This file holds the implementation of the action class
and its subclasses. Actions are used to store information
about entity movement/attacks/other.
"""


class Action:
    """Base action class."""


class Surge(Action):
    """Base class for any action with a direction."""

    def __init__(self, dx, dy):
        super().__init__()
        self.dx = dx
        self.dy = dy


class Move(Surge):
    """Movement to an adjacent tile."""

    def __init__(self, dx, dy):
        super().__init__(dx, dy)


class Attack(Action):
    """Melee attack."""

    def __init__(self, other):
        super().__init__()
        self.other = other


class PickUp(Action):
    """Pick up something from the floor."""


class Wait(Action):
    """Do nothing."""


class OpenMenu(Action):
    """Open a menu."""
