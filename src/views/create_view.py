from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.create_controller import CustomerCreateControllerInterface
from src.main.validators.create_customer_validator import create_customer_validator

class CreateView(ViewInterface):
    def __init__(self, controller: CustomerCreateControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        create_customer_validator(http_request)

        customer_info = http_request.body
        body_response = self.__controller.create(customer_info)

        return HttpResponse(status_code=201, body=body_response)
