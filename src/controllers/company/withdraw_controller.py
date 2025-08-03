# pylint: disable=broad-exception-caught
from src.models.interfaces.customer import CustomerInterface
from src.controllers.interfaces.withdraw_controller import CustomerWithdrawControllerInterface
from src.main.errors.errors_types.http_bad_request import HttpBadRequestError
from src.main.errors.errors_types.http_not_found import HttpNotFoundError

class CompanyWithdrawController(CustomerWithdrawControllerInterface):
    def __init__(self, company_repository: CustomerInterface) -> None:
        self.__company_repository = company_repository

    def withdraw(self, customer_id: int, value: float) -> dict:
        self.__validate_value(value)
        is_valid_withdraw = self.__decrease_balance_in_db(customer_id, value)
        response = self.__format_response(is_valid_withdraw)

        return response

    def __validate_value(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise HttpBadRequestError("Value not number")

        if value <= 0:
            raise HttpBadRequestError("Value not is valid")

    def __decrease_balance_in_db(self, customer_id: int, value: float) -> bool:
        try:
            is_withdraw = self.__company_repository.withdraw(customer_id, value)

            if not is_withdraw:
                raise HttpNotFoundError("Customer not found")

            return is_withdraw
        except Exception as exception:
            raise exception

    def __format_response(self, is_valid_withdraw: bool) -> dict:
        return {
            "data": {
                "type": "Company",
                "count": 1,
                "attributes": {
                    "valid": is_valid_withdraw
                }
            }
        }
