from abc import ABC, abstractmethod

class CustomerCreateControllerInterface(ABC):

    @abstractmethod
    def create(self, customer_info: dict) -> dict:
        pass
