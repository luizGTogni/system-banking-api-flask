from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .list_all_view import ListAllView

class MockController:
    def list_all(self) -> dict:
        return {
            "data": {
                "type": "Individual",
                "count": 2,
                "attributes": [
                    {
                        "name": "John Doe",
                        "age": 25,
                        "phone": "19999999999",
                        "email": "johndoe@example.com",
                        "category": "Category A",
                        "monthly_income": 22000
                    },
                    {
                        "name": "Bryan Doe",
                        "age": 35,
                        "phone": "19999999999",
                        "email": "brayndoe@example.com",
                        "category": "Category C",
                        "monthly_income": 12000
                    },
                ]
            }
        }

def test_list_all_view():
    mock_controller = MockController()
    view = ListAllView(controller=mock_controller)

    http_response = view.handle(HttpRequest())

    assert isinstance(http_response, HttpResponse)
    assert http_response.status_code == 200
    assert http_response.body == {
        "data": {
            "type": "Individual",
            "count": 2,
            "attributes": [
                {
                    "name": "John Doe",
                    "age": 25,
                    "phone": "19999999999",
                    "email": "johndoe@example.com",
                    "category": "Category A",
                    "monthly_income": 22000
                },
                {
                    "name": "Bryan Doe",
                    "age": 35,
                    "phone": "19999999999",
                    "email": "brayndoe@example.com",
                    "category": "Category C",
                    "monthly_income": 12000
                },
            ]
        }
    }
