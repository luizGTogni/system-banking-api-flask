# pylint: disable=unused-argument
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .generate_report_view import GenerateReportView

class MockController:
    def generate_report(self, customer_id: int) -> dict:
        return {
            "data": {
                "type": "Individual",
                "count": 1,
                "attributes": {
                    "name": "John Doe",
                    "category": "Category A",
                    "balance": 22000
                }
            }
        }

def test_generate_report_view():
    mock_controller = MockController()
    view = GenerateReportView(controller=mock_controller)

    htt_request = HttpRequest(param={ "customer_id": 10 })

    http_response = view.handle(htt_request)

    assert isinstance(http_response, HttpResponse)
    assert http_response.status_code == 200
    assert http_response.body == {
        "data": {
            "type": "Individual",
            "count": 1,
            "attributes": {
                "name": "John Doe",
                "category": "Category A",
                "balance": 22000
            }
        }
    }
