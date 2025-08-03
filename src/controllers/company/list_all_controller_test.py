from src.controllers.mocks.mock_repository import MockCompanyRepository
from src.controllers.mocks.mock_repository import MockCompanyRepositoryError
from .list_all_controller import CompanyListAllController

def test_list_all_customers_controller():
    mock_repository = MockCompanyRepository()
    controller = CompanyListAllController(company_repository=mock_repository)
    response = controller.list_all()

    print(response)

    assert response == {
        "data": {
            "type": "Companies",
            "count": 2,
            "attributes": [
                {
                    "id": 1,
                    "name":"John Doe",
                    "age":25,
                    "phone":"19999999999",
                    "email":"johndoe@example.com",
                    "category":"Category A",
                    "monthly_income":6500.00,
                    "balance":1500.00
                },
                {
                    "id": 2,
                    "name":"Bryan Doe",
                    "age":35,
                    "phone":"19999999999",
                    "email":"bryandoe@example.com",
                    "category":"Category C",
                    "monthly_income":10500.00,
                    "balance":15000.00
                },
            ]
        }
    }

def test_list_all_customers_controller_error_not_found():
    mock_repository = MockCompanyRepositoryError()
    controller = CompanyListAllController(company_repository=mock_repository)
    response = controller.list_all()

    assert response == {
        "data": {
            "type": "Companies",
            "count": 0,
            "attributes": []
        }
    }
