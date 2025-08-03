from src.models.interfaces.customer import CustomerInterface
from src.models.sqlalchemy.entities.individual import IndividualTable
from src.controllers.interfaces.list_all_controller import CustomerListAllControllerInterface

class IndividualListAllController(CustomerListAllControllerInterface):
    def __init__(self, individual_repository: CustomerInterface) -> None:
        self.__individual_repository = individual_repository

    def list_all(self) -> dict:
        customers = self.__get_individuals_in_db()
        response = self.__format_response(customers)

        return response

    def __get_individuals_in_db(self) -> list[IndividualTable]:
        customers = self.__individual_repository.list_all()
        return customers

    def __format_response(self, customers: list[IndividualTable]) -> dict:
        formatted_customers = []

        for customer in customers:
            formatted_customers.append({
                "id": customer.id,
                "name": customer.full_name,
                "age": customer.age,
                "phone": customer.phone,
                "email": customer.email,
                "category": customer.category,
                "monthly_income": customer.monthly_income,
                "balance": customer.balance
            })

        return {
            "data": {
                "type": "Individuals",
                "count": len(formatted_customers),
                "attributes": formatted_customers
            }
        }
