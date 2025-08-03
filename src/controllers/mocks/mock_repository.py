# pylint: disable=unused-argument

from src.models.sqlalchemy.entities.individual import IndividualTable
from src.models.sqlalchemy.entities.company import CompanyTable

class MockCustomerRepository:
    def create(
        self,
        name: str,
        age: int,
        phone: str,
        email: str,
        category: str,
        monthly_income: float
    ) -> None:
        pass

    def generate_report(self, customer_id: int) -> dict:
        return {
            "name": "John Doe",
            "category": "Category A",
            "balance": 100
        }

    def withdraw(self, customer_id: int, value: float) -> bool:
        return True

class MockIndividualRepository:
    def list_all(self) -> list:
        return [
            IndividualTable(
                id=1,
                full_name="John Doe",
                age=25,
                phone="19999999999",
                email="johndoe@example.com",
                category="Category A",
                monthly_income=6500.00,
                balance=1500.00
            ),
            IndividualTable(
                id=2,
                full_name="Bryan Doe",
                age=35,
                phone="19999999999",
                email="bryandoe@example.com",
                category="Category C",
                monthly_income=10500.00,
                balance=15000.00
            ),
        ]

class MockIndividualRepositoryError:
    def list_all(self) -> list:
        return []

class MockCompanyRepository:
    def list_all(self) -> list:
        return [
            CompanyTable(
                id=1,
                trade_name="John Doe",
                age=25,
                phone="19999999999",
                corporate_email="johndoe@example.com",
                category="Category A",
                monthly_income=6500.00,
                balance=1500.00
            ),
            CompanyTable(
                id=2,
                trade_name="Bryan Doe",
                age=35,
                phone="19999999999",
                corporate_email="bryandoe@example.com",
                category="Category C",
                monthly_income=10500.00,
                balance=15000.00
            ),
        ]

class MockCompanyRepositoryError:
    def list_all(self) -> list:
        return []
