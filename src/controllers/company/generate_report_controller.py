from src.controllers.interfaces.report_controller import CustomerGenerateReportControlerInterface
from src.models.interfaces.customer import CustomerInterface

class CompanyGenerateReportController(CustomerGenerateReportControlerInterface):
    def __init__(self, company_repository: CustomerInterface) -> None:
        self.__company_repository = company_repository

    def generate_report(self, customer_id: int) -> dict:
        report = self.__collect_report_in_db(customer_id)
        response = self.__format_response(report)

        return response

    def __collect_report_in_db(self, customer_id: int) -> dict:
        report = self.__company_repository.generate_report(customer_id)
        return report

    def __format_response(self, report: dict) -> dict:
        return {
            "data": {
                "type": "Company",
                "count": 1,
                "attributes": report
            }
        }
