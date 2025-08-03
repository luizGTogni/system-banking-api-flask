from pytest import raises
from src.controllers.mocks.mock_repository import MockCustomerRepository
from .withdraw_controller import CompanyWithdrawController

def test_withdraw():
    mock_repository = MockCustomerRepository()
    controller = CompanyWithdrawController(company_repository=mock_repository)
    response = controller.withdraw(customer_id=10, value=100)

    assert response == {
        "data": {
            "type": "Company",
            "count": 1,
            "attributes": {
                "valid": True
            }
        }
    }

def test_withdraw_validate_value_not_number():
    mock_repository = MockCustomerRepository()
    controller = CompanyWithdrawController(company_repository=mock_repository)

    with raises(Exception) as excinfo:
        controller.withdraw(customer_id=10, value="A")

    assert str(excinfo.value) == "Value not number"

def test_withdraw_validate_value_not_is_valid():
    mock_repository = MockCustomerRepository()
    controller = CompanyWithdrawController(company_repository=mock_repository)

    with raises(Exception) as excinfo:
        controller.withdraw(customer_id=10, value=-1)

    assert str(excinfo.value) == "Value not is valid"
