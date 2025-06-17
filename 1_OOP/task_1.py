

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        """пополнение счёта"""
        self.__balance += amount
        return self.__balance


    def withdraw(self, amount):
        """снятие средств (не должно позволять уйти в минус)"""
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return "Недостаточно средств"


    def get_balance(self):
        """получить текущий баланс"""
        return self.__balance


a = BankAccount(100)
print(a.deposit(100))
print(a.withdraw(100))
print(a.withdraw(10000))
print(a.get_balance())
