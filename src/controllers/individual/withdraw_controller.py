from src.models.interfaces.customer import CustomerInterface
from src.controllers.interfaces.withdraw_controller import CustomerWithdrawControllerInterface

class IndividualWithdrawController(CustomerWithdrawControllerInterface):
    def __init__(self, individual_repository: CustomerInterface) -> None:
        self.__individual_repository = individual_repository

    def withdraw(self, customer_id: int, value: float) -> dict:
        self.__validate_value(value)
        is_valid_withdraw = self.__decrease_balance_in_db(customer_id, value)
        response = self.__format_response(is_valid_withdraw)

        return response

    def __validate_value(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            raise Exception("value not number")

        if value <= 0:
            raise Exception("value not is valid")

    def __decrease_balance_in_db(self, customer_id: int, value: float) -> bool:
        return self.__individual_repository.withdraw(customer_id, value)

    def __format_response(self, is_valid_withdraw: bool) -> dict:
        return {
            "data": {
                "type": "Individual",
                "count": 1,
                "attributes": {
                    "valid": is_valid_withdraw
                }
            }
        }
