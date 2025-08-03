from pytest import raises
from src.main.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .create_customer_validator import create_customer_validator

class MockRequest:
    def __init__(self, body: dict) -> None:
        self.body = body

def test_create_customer_validator():
    mock_request = MockRequest({
        "name": "John Doe",
        "age": 25,
        "phone": "19999999999",
        "email": "johndoe@example.com",
        "category": "Category A",
        "monthly_income": 22000
    })

    create_customer_validator(mock_request)

def test_create_customer_validator_error_name():
    mock_request = MockRequest({
        "name": "",
        "age": 25,
        "phone": "19999999999",
        "email": "johndoe@example.com",
        "category": "Category A",
        "monthly_income": 22000
    })

    with raises(HttpUnprocessableEntityError):
        create_customer_validator(mock_request)

def test_create_customer_validator_error_less_than_18():
    mock_request = MockRequest({
        "name": "John Doe",
        "age": 17,
        "phone": "19999999999",
        "email": "johndoe@example.com",
        "category": "Category A",
        "monthly_income": 22000
    })

    with raises(HttpUnprocessableEntityError):
        create_customer_validator(mock_request)

def test_create_customer_validator_error_phone_not_valid():
    mock_request = MockRequest({
        "name": "John Doe",
        "age": 25,
        "phone": "19999999",
        "email": "johndoe@example.com",
        "category": "Category A",
        "monthly_income": 22000
    })

    with raises(HttpUnprocessableEntityError):
        create_customer_validator(mock_request)

def test_create_customer_validator_error_email_not_valid():
    mock_request = MockRequest({
        "name": "John Doe",
        "age": 25,
        "phone": "19999999999",
        "email": "johndoe",
        "category": "Category A",
        "monthly_income": 22000
    })

    with raises(HttpUnprocessableEntityError):
        create_customer_validator(mock_request)

def test_create_customer_validator_error_category():
    mock_request = MockRequest({
        "name": "John Doe",
        "age": 25,
        "phone": "19999999999",
        "email": "johndoe@example.com",
        "category": "",
        "monthly_income": 22000
    })

    with raises(HttpUnprocessableEntityError):
        create_customer_validator(mock_request)

def test_create_customer_validator_error_income_less_than_0():
    mock_request = MockRequest({
        "name": "John Doe",
        "age": 25,
        "phone": "19999999999",
        "email": "johndoe@example.com",
        "category": "Category A",
        "monthly_income": -1
    })

    with raises(HttpUnprocessableEntityError):
        create_customer_validator(mock_request)
