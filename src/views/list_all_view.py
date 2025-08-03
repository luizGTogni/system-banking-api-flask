from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.list_all_controller import CustomerListAllControllerInterface

class ListAllView(ViewInterface):
    def __init__(self, controller: CustomerListAllControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list_all()

        return HttpResponse(status_code=200, body=body_response)
