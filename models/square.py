#!/usr/bin/python3
"""
Defines a square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represent a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square.
        """
        if args and len(args) != 0:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                else: continue

        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                # removed the break statement, incase if the passed args are greater
                # than 5, and one of the attributes is at the end

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        square_dict = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

        return square_dict

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)