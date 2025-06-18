from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):

    def speak(self):
        return "Woof!"

    def move(self):
        return "бегает"


class Bird(Animal):

    def speak(self):
        return "Tweet!"

    def move(self):
        return "летает"


class Fish(Animal):

    def speak(self):
        return ""

    def move(self):
        return "плавает"


animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(f"{animal.__class__.__name__}:")
    print(f"  Звук: {animal.speak()}")
    print(f"  Движение: {animal.move()}")
    print("")  # Пустая строка для разделения