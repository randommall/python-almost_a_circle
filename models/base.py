#!/usr/bin/python3
"""
Defines a base model class.
"""
import json
import csv
import turtle

class Base:
    """
    Represents the base model
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        to_json = json.dumps(list_dictionaries)

        return to_json

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): List of instances who inherits of Base
        """
        file_name = "{}.json".format(cls.__name__)

        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                jsonfile.write(Base.to_json_string(list_dict))

    def from_json_string(json_string):
        """

        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)

            return dummy

    @classmethod
    def load_from_file(cls):
        """

        """
        file_name = "{}.json".format(cls.__name__)

        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())

                list_instances = []

                for d in list_dicts:
                    list_instances.append(cls.create(**d))
                return list_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV serialization of a list of objects to a file.
        """
        # corrected the name of the file extension from .json to .csv
        file_name = "{}.csv".format(cls.__name__)

        with open(file_name, "w") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)

            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a CSV file.
        """
        # corrected the name of the file extension from .json to .csv
        file_name = "{}.csv".format(cls.__name__)
        
        try:
            with open(file_name, "r") as csvfile:
                if cls.__name__ == "Rectangle":
                    filednames = ["id", "width", "height", "x", "y"]
                else:
                    filednames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=filednames)

                new_list_dict = []

                converted_dict = {}

                for d in list_dicts:
                    for key, value in d.items():
                        converted_dict[key] = int(value)

                    new_list_dict.append(converted_dict)

                list_dicts = new_list_dict

                list_of_instances = []

                for d in list_dicts:
                    list_of_instances.append(cls.create(**d))

                return list_of_instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles,
        and Squares using the turtle module.
        """
        turt = turtle.Turtle()

        turt.screen.bgcolor("#3399FF")

        turt.pensize(4)

        turt.shape("turtle")

        for rect in list_rectangles:
            turt.showturtle()

            turt.up()

            turt.goto(rect.x, rect.y)

            turt.down()

            for _ in range(2):
                turt.forward(rect.width)

                turt.left(90)

                turt.forward(rect.height)

                turt.left(90)

            turt.hideturtle()


        turt.color("#FFFF00")

        for sq in list_squares:
            turt.showturtle()

            turt.up()

            turt.goto(sq.x, sq.y)

            turt.down()

            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)

                turt.forward(sq.height)

                turt.left(90)

            turt.hideturtle()

        turtle.exitonclick()










































if __name__ == "__main__":

    pass
