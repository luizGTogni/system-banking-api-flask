from abc import ABC, abstractmethod

class CustomerInterface(ABC):

    @abstractmethod
    def create(
        self,
        name: str,
        age: int,
        phone: str,
        email: str,
        category: str,
        revenue: float
    ) -> None:
        pass

    @abstractmethod
    def list_all(self) -> list:
        pass

    @abstractmethod
    def generate_report(self, customer_id: int) -> dict:
        pass

    @abstractmethod
    def withdraw(self, customer_id: int, value: float) -> bool:
        pass
