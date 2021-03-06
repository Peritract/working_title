"""
This file contains the implementation of the basic
"Object" class - any thing that exists in the game
world.
"""

from .constants import COLOURS as C, RenderOrder


class Object:

    def __init__(self,
                 name="thing",
                 description="A nondescript object.",
                 x=0,
                 y=0,
                 char="%",
                 colour=C["TEMP"],
                 blocks=True,
                 area=None,
                 render_order=RenderOrder.FEATURE):

        """Sets key properties"""
        self.name = name
        self.description = description
        self.x = x
        self.y = y
        self.char = char
        self.colour = colour
        self.blocks = blocks
        self.area = area
        self.render_order = render_order

    @property
    def loc(self):
        """Return's the objects x and y as a tuple)."""
        return (self.x, self.y)

    def set_loc(self, x, y):
        """Sets the object location."""
        if self.area.in_bounds(x, y):
            self.x = x
            self.y = y

    @property
    def description_text(self):
        """Returns the description for display."""
        return self.description

    def destroy(self):
        """Remove from the game."""
        if self.area:
            self.area.remove_contents(self)
            self.area = None
