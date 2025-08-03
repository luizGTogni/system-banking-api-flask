from src.views.interfaces.view_interface import ViewInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.report_controller import CustomerGenerateReportControlerInterface

class GenerateReportView(ViewInterface):
    def __init__(self, controller: CustomerGenerateReportControlerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        customer_id = http_request.param["customer_id"]
        body_response = self.__controller.generate_report(customer_id)

        return HttpResponse(status_code=200, body=body_response)
