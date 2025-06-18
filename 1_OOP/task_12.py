

class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """
        Создает класса из градусов Фаренгейта.
        """
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @property
    def kelvin(self):
        """
        Возвращает температуру в Кельвинах.
        """
        return self.celsius + 273.15

    @staticmethod
    def is_freezing(celsius):
        """
        Проверяет, является ли температура точкой замерзания воды (0°C или ниже).
        """
        return celsius <= 0


temp = Temperature.from_fahrenheit(10)
print(temp.celsius)
print(temp.kelvin)
print(Temperature.is_freezing(100))

