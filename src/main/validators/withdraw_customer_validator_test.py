from pytest import raises
from src.main.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .withdraw_customer_validator import withdraw_customer_validator

class MockRequest:
    def __init__(self, body: dict) -> None:
        self.body = body

def test_withdraw_customer_validator():
    mock_request = MockRequest({
        "value": 100,
    })

    withdraw_customer_validator(mock_request)

def test_withdraw_customer_validator_error():
    mock_request = MockRequest({
        "value": 0,
    })

    with raises(HttpUnprocessableEntityError):
        withdraw_customer_validator(mock_request)
