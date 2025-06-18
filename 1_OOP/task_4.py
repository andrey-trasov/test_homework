from abc import ABC, abstractmethod

class Transport(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Car(Transport):

    def start_engine(self):
        return "Автомобиль: двигатель запущен"

    def stop_engine(self):
        return "Автомобиль: двигатель остановлен"

    def move(self):
        return "Автомобиль: едет по дороге"


class Boat(Transport):

    def start_engine(self):
        return "Лодка: двигатель запущен"

    def stop_engine(self):
        return "Лодка: двигатель остановлен"

    def move(self):
        return "Лодка: плывет по воде"



my_car = Car()
my_boat = Boat()

print(my_car.start_engine())
print(my_car.move())
print(my_car.stop_engine())

print("\n")

print(my_boat.start_engine())
print(my_boat.move())
print(my_boat.stop_engine())