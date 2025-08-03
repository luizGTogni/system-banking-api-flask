# pylint: disable=unused-argument
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .withdraw_view import WithdrawView

class MockController:
    def withdraw(self, customer_id: int, value: float) -> dict:
        return {
            "data": {
                "type": "Individual",
                "count": 2,
                "attributes": {
                    "valid": True
                }
            }
        }

def test_list_all_view():
    mock_controller = MockController()
    view = WithdrawView(controller=mock_controller)

    http_request = HttpRequest(body={ "value": 100 }, param={ "customer_id": 10 })

    http_response = view.handle(http_request)

    assert isinstance(http_response, HttpResponse)
    assert http_response.status_code == 200
    assert http_response.body == {
        "data": {
            "type": "Individual",
            "count": 2,
            "attributes": {
                "valid": True
            }
        }
    }
