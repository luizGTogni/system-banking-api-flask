from src.models.interfaces.customer import CustomerInterface
from src.controllers.interfaces.customer_create_controller import CustomerCreateControllerInterface

class IndividualCreateController(CustomerCreateControllerInterface):
    def __init__(self, individual_repository: CustomerInterface) -> None:
        self.__individual_repository = individual_repository

    def create(self, customer_info: dict) -> dict:
        name = customer_info["name"]
        age = customer_info["age"]
        phone = customer_info["phone"]
        email = customer_info["email"]
        category = customer_info["category"]
        monthly_income = customer_info["monthly_income"]

        self.__insert_customer_in_db(name, age, phone, email, category, monthly_income)
        response = self.__format_response(customer_info)

        return response

    def __insert_customer_in_db(
            self,
            name: str,
            age: int,
            phone: str,
            email: str,
            category: str,
            monthly_income: float
    ) -> None:
        self.__individual_repository.create(
            name=name,
            age=age,
            phone=phone,
            email=email,
            category=category,
            monthly_income=monthly_income
        )

    def __format_response(self, customer_info: dict) -> dict:
        return {
            "data": {
                "type": "Individual",
                "count": 1,
                "attributes": customer_info,
            }
        }
