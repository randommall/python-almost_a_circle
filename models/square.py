#!/usr/bin/python3
"""
Module for square class
"""
from rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Square class constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the Square.
        """
        self.width = value
        self.height = value

    def updated(self, *args, **kwargs):
        """
        Assign arguments to attributes based on their positions.
        """
        if args:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                else:
                    continue
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
                else:
                    break

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.
        """
        square_dict = {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
        }

        return square_dict


    def __str__(self):
        """
        Str representation
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)



if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)
