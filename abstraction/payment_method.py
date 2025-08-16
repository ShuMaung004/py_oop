from abc import ABC,abstractmethod

# Abstract class
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

    @abstractmethod
    def refund(self,amount):
        pass

