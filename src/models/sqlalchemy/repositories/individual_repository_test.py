from pytest import raises
from src.models.sqlalchemy.entities.individual import IndividualTable
from .individual_repository import IndividualRepository
from .mocks.mock_connection import MockConnection
from .mocks.mock_connection_exception import MockConnectionException
from .mocks.mock_connection_exception import MockConnectionQueryException

def test_create_individual():
    mock_connection = MockConnection()
    repository = IndividualRepository(db_connection=mock_connection)
    repository.create(
        name="John Doe",
        age=25,
        phone="19999999999",
        email="johndoe@example.com",
        category="Category A",
        monthly_income=6500.00
    )

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()
    parameters = mock_connection.session.add.call_args

    individual_created = parameters[0][0]

    assert individual_created.full_name == "John Doe"
    assert individual_created.age == 25
    assert individual_created.phone == "19999999999"
    assert individual_created.email == "johndoe@example.com"
    assert individual_created.category == "Category A"
    assert individual_created.monthly_income == 6500.00

def test_create_individual_exception():
    mock_connection = MockConnectionException()
    repository = IndividualRepository(db_connection=mock_connection)

    with raises(Exception):
        repository.create(
            name="John Doe",
            age=25,
            phone="19999999999",
            email="johndoe@example.com",
            category="Category A",
            monthly_income=6500.00
        )

    mock_connection.session.rollback.assert_called_once()

def test_list_all_individuals():
    mock_connection = MockConnection()

    mock_connection.session.add(IndividualTable(
        id=1,
        full_name="John Doe",
        age=25,
        phone="19999999999",
        email="johndoe@example.com",
        category="Category A",
        monthly_income=6500.00,
        balance=0
    ))

    mock_connection.session.add(IndividualTable(
        id=2,
        full_name="John Doe",
        age=25,
        phone="19999999999",
        email="johndoe@example.com",
        category="Category A",
        monthly_income=6500.00,
        balance=0
    ))

    mock_connection.session.commit()

    repository = IndividualRepository(db_connection=mock_connection)
    response = repository.list_all()

    mock_connection.session.query.assert_called_once_with(IndividualTable)
    mock_connection.session.all.assert_called_once()

    assert len(response) == 2
    assert response[0].id == 1
    assert response[1].id == 2

def test_list_all_individuals_not_found():
    mock_connection = MockConnectionException()
    repository = IndividualRepository(db_connection=mock_connection)
    response = repository.list_all()

    mock_connection.session.query.assert_called_once_with(IndividualTable)
    mock_connection.session.all.assert_not_called()

    assert response == []

def test_generate_report():
    mock_connection = MockConnection()

    mock_connection.session.add(IndividualTable(
        id=10,
        full_name="John Doe",
        age=25,
        phone="19999999999",
        email="johndoe@example.com",
        category="Category A",
        monthly_income=6500.00,
        balance=1500.00
    ))

    repository = IndividualRepository(db_connection=mock_connection)
    response = repository.generate_report(customer_id=10)

    mock_connection.session.query.assert_called_once_with(IndividualTable)
    mock_connection.session.filter_by.assert_called_once_with(id=10)
    mock_connection.session.one.assert_called_once()

    assert response["name"] == "John Doe"
    assert response["category"] == "Category A"
    assert response["balance"] == 1500.00

def test_generate_report_not_found():
    mock_connection = MockConnectionException()
    repository = IndividualRepository(db_connection=mock_connection)
    response = repository.generate_report(customer_id=10)

    mock_connection.session.query.assert_called_once_with(IndividualTable)
    mock_connection.session.filter_by.assert_not_called()

    assert isinstance(response, dict)
    assert not response

def test_withdraw():
    mock_connection = MockConnection()
    mock_connection.session.add(IndividualTable(
        id=10,
        full_name="John Doe",
        age=25,
        phone="19999999999",
        email="johndoe@example.com",
        category="Category A",
        monthly_income=6500.00,
        balance=1500.00
    ))

    repository = IndividualRepository(db_connection=mock_connection)
    response = repository.withdraw(customer_id=10, value=150)

    mock_connection.session.query.assert_called_once_with(IndividualTable)
    mock_connection.session.filter_by.assert_called_once_with(id=10)
    mock_connection.session.one.assert_called_once()

    assert response is True

def test_withdraw_error_value_bigger_balance():
    mock_connection = MockConnection()
    mock_connection.session.add(IndividualTable(
        id=10,
        full_name="John Doe",
        age=25,
        phone="19999999999",
        email="johndoe@example.com",
        category="Category A",
        monthly_income=6500.00,
        balance=100.00
    ))


    repository = IndividualRepository(db_connection=mock_connection)
    with raises(Exception):
        repository.withdraw(customer_id=10, value=150)

    mock_connection.session.query.assert_called_once_with(IndividualTable)
    mock_connection.session.filter_by.assert_called_once_with(id=10)
    mock_connection.session.one.assert_called_once()

def test_withdraw_error_value_bigger_limit():
    mock_connection = MockConnection()
    mock_connection.session.add(IndividualTable(
        id=10,
        full_name="John Doe",
        age=25,
        phone="19999999999",
        email="johndoe@example.com",
        category="Category A",
        monthly_income=6500.00,
        balance=1500.00
    ))

    repository = IndividualRepository(db_connection=mock_connection)

    with raises(Exception):
        repository.withdraw(customer_id=10, value=550)

    mock_connection.session.query.assert_called_once_with(IndividualTable)
    mock_connection.session.filter_by.assert_called_once_with(id=10)
    mock_connection.session.one.assert_called_once()

def test_withdraw_exception():
    mock_connection = MockConnectionQueryException()
    repository = IndividualRepository(db_connection=mock_connection)

    with raises(Exception):
        repository.withdraw(customer_id=10, value=150)

    mock_connection.session.rollback.assert_called_once()
