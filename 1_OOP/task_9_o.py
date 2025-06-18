from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def payment(self, partnership):
        pass


class PayPal(Payment):

    def payment(self, partnership):
        return f"оплата {partnership} рублей через PayPal"

class CreditCard(Payment):

    def payment(self, partnership):
        return f"оплата {partnership} рублей через CreditCard"

class Crypto(Payment):

    def payment(self, partnership):
        return f"оплата {partnership} рублей через Crypto"


class PaymentProcessor:

    def __init__(self, payment: Payment):
        self.payment = payment


    def pay(self, partnership):
        return self.payment.payment(partnership)

paypal = PaymentProcessor(PayPal())
print(paypal.pay(1000))

creditcard = PaymentProcessor(CreditCard())
print(creditcard.pay(1000))

crypto = PaymentProcessor(Crypto())
print(crypto.pay(1000))