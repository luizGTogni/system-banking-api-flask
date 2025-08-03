from src.models.sqlalchemy.settings.connection import db_connection_handler
from src.models.sqlalchemy.repositories.company_repository import CompanyRepository
from src.controllers.company.generate_report_controller import CompanyGenerateReportController
from src.views.generate_report_view import GenerateReportView

def company_gen_report_view_composer():
    repository = CompanyRepository(db_connection=db_connection_handler)
    controller = CompanyGenerateReportController(company_repository=repository)
    view = GenerateReportView(controller)

    return view
