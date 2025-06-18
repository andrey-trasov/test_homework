

class Flyable:

    def fly(self):
        return "I'm flying!"


class Swimmable:

    def swim(self):
        return "I'm swimming!"

class Duck(Flyable, Swimmable):

    def make_sound(self):
        return "Quack!"

duck = Duck()
print(duck.fly())
print(duck.swim())
print(duck.make_sound())
