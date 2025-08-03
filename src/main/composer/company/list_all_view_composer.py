from src.models.sqlalchemy.settings.connection import db_connection_handler
from src.models.sqlalchemy.repositories.company_repository import CompanyRepository
from src.controllers.company.list_all_controller import CompanyListAllController
from src.views.list_all_view import ListAllView

def company_list_all_view_composer():
    repository = CompanyRepository(db_connection=db_connection_handler)
    controller = CompanyListAllController(company_repository=repository)
    view = ListAllView(controller)

    return view
