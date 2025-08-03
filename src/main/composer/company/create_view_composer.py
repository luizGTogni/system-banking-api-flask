from src.models.sqlalchemy.settings.connection import db_connection_handler
from src.models.sqlalchemy.repositories.company_repository import CompanyRepository
from src.controllers.company.create_controller import CompanyCreateController
from src.views.create_view import CreateView

def company_create_view_composer():
    repository = CompanyRepository(db_connection=db_connection_handler)
    controller = CompanyCreateController(company_repository=repository)
    view = CreateView(controller)

    return view
