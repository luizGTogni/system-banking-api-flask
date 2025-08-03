from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.withdraw_controller import CustomerWithdrawControllerInterface

class WithdrawView(ViewInterface):
    def __init__(self, controller: CustomerWithdrawControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        customer_id = http_request.param["customer_id"]
        value = http_request.body["value"]
        body_response = self.__controller.withdraw(customer_id=customer_id, value=value)

        return HttpResponse(status_code=200, body=body_response)
