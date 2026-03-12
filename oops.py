from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class creditcard(payment):
    def pay(self):
        print("Credit card payment")
c = creditcard()
c.pay()
class UPI(payment):
    def pay(self):
        print("UPI payment")
u=UPI()
u.pay()

from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car start")
c=car()
c.start()