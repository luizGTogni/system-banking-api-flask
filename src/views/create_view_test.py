from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .create_view import CreateView

class MockController:
    def create(self, customer_info: dict) -> dict:
        return {
            "data": {
                "type": "Individual",
                "count": 1,
                "attributes": customer_info,
            }
        }

def test_create_view():
    mock_controller = MockController()
    view = CreateView(controller=mock_controller)

    http_request = HttpRequest(body={
        "name": "John Doe",
        "age": 25,
        "phone": "19999999999",
        "email": "johndoe@example.com",
        "category": "Category A",
        "monthly_income": 22000
    })

    http_response = view.handle(http_request)

    assert isinstance(http_response, HttpResponse)
    assert http_response.status_code == 201
    assert http_response.body == {
        "data": {
            "type": "Individual",
            "count": 1,
            "attributes": {
                "name": "John Doe",
                "age": 25,
                "phone": "19999999999",
                "email": "johndoe@example.com",
                "category": "Category A",
                "monthly_income": 22000
            }
        }
    }
