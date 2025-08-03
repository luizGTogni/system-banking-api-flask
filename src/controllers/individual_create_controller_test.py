from .individual_create_controller import IndividualCreateController
from .mocks.mock_repository import MockCustomerRepository

def test_create_customer_controller():
    mock_repository = MockCustomerRepository()
    controller = IndividualCreateController(individual_repository=mock_repository)

    customer_info = {
        "name": "John Doe",
        "age": 25,
        "email": "johndoe@example.com",
        "phone": "19999999999",
        "category": "Category A",
        "monthly_income": 1500.0
    }

    response = controller.create(customer_info)

    assert response == {
        "data": {
            "type": "Individual",
            "count": 1,
            "attributes": {
                "name": "John Doe",
                "age": 25,
                "email": "johndoe@example.com",
                "phone": "19999999999",
                "category": "Category A",
                "monthly_income": 1500.0
            }
        }
    }
