from abc import ABC, abstractmethod


class Bird(ABC):

    @abstractmethod
    def print_name(self):
        pass


class Sparrow(Bird):

    def print_name(self):
        return "Класс воробья "

class Penguin(Bird):

    def print_name(self):
        return "Класс пингвина "



sparrow = Sparrow()
print(sparrow.print_name())

penguin = Penguin()
print(penguin.print_name())


