from abc import ABC, abstractmethod

class OnlinePaymentService(ABC):
    @abstractmethod
    def payment_fee(self, amount):
        pass

    @abstractmethod
    def interest(self, amount, months):
        pass
