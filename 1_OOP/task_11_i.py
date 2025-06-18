from abc import ABC, abstractmethod


class Animal_fly(ABC):

    @abstractmethod
    def fly(self):
        pass

class Animal_run(ABC):

    @abstractmethod
    def run(self):
        pass

class Animal_swim(ABC):

    @abstractmethod
    def swim(self):
        pass


class Lion(Animal_run):

    def run(self):
        return "Лев бежит"

lion = Lion()
print(lion.run())

