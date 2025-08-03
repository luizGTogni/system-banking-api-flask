from src.models.interfaces.customer import CustomerInterface
from src.models.sqlalchemy.entities.company import CompanyTable
from src.controllers.interfaces.list_all_controller import CustomerListAllControllerInterface

class CompanyListAllController(CustomerListAllControllerInterface):
    def __init__(self, company_repository: CustomerInterface) -> None:
        self.__company_repository = company_repository

    def list_all(self) -> dict:
        customers = self.__get_companys_in_db()
        response = self.__format_response(customers)

        return response

    def __get_companys_in_db(self) -> list[CompanyTable]:
        customers = self.__company_repository.list_all()
        return customers

    def __format_response(self, customers: list[CompanyTable]) -> dict:
        formatted_customers = []

        for customer in customers:
            formatted_customers.append({
                "id": customer.id,
                "name": customer.trade_name,
                "age": customer.age,
                "phone": customer.phone,
                "email": customer.corporate_email,
                "category": customer.category,
                "monthly_income": customer.monthly_income,
                "balance": customer.balance
            })

        return {
            "data": {
                "type": "Companies",
                "count": len(formatted_customers),
                "attributes": formatted_customers
            }
        }
