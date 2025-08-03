from src.models.sqlalchemy.settings.connection import db_connection_handler
from src.models.sqlalchemy.repositories.individual_repository import IndividualRepository
from src.controllers.individual.generate_report_controller import IndividualGenerateReportController
from src.views.generate_report_view import GenerateReportView

def individual_generate_report_view_composer():
    repository = IndividualRepository(db_connection=db_connection_handler)
    controller = IndividualGenerateReportController(individual_repository=repository)
    view = GenerateReportView(controller)

    return view
