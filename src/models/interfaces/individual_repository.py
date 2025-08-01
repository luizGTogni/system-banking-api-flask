from abc import ABC, abstractmethod
from src.models.sqlalchemy.entities.individual import IndividualTable

class IndividualRepositoryInterface(ABC):
    @abstractmethod
    def create(
        self,
        full_name: str,
        age: int,
        phone: str,
        email: str,
        category: str,
        monthly_income: float
    ) -> None:
        pass

    @abstractmethod
    def list_all(self) -> list[IndividualTable]:
        pass
