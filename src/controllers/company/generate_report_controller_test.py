from src.controllers.mocks.mock_repository import MockCustomerRepository
from .generate_report_controller import CompanyGenerateReportController

def test_generate_report():
    mock_repository = MockCustomerRepository()
    controller = CompanyGenerateReportController(company_repository=mock_repository)
    response = controller.generate_report(customer_id=10)

    assert response == {
        "data": {
            "type": "Company",
            "count": 1,
            "attributes": {
                "name": "John Doe",
                "category": "Category A",
                "balance": 100,
            }
        }
    }
