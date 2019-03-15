# Name mangling


class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi"  # Private property
        self.__msg = "I like turtles!"  # Name mangling
        self.__lol = "AHAHAHA"  # Name mangling


# Class attributes vs. instance attributes
class Chicken():

    total_eggs = 0

    def __init__(self, name, species):
        self.species = species
        self.name = name
        self.eggs = 0

    def lay_egg(self):
        Chicken.total_eggs += 1
        self.eggs += 1
        return self.eggs
