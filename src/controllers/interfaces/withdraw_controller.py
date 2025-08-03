from abc import ABC, abstractmethod

class CustomerWithdrawControllerInterface(ABC):

    @abstractmethod
    def withdraw(self, customer_id: int, value: float) -> dict:
        pass
