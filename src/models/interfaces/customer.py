from abc import ABC, abstractmethod

class CustomerInterface(ABC):

    @abstractmethod
    def generate_report(self) -> None:
        pass

    @abstractmethod
    def withdraw(self, value: float) -> None:
        pass
