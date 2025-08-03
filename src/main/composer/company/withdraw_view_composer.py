from src.models.sqlalchemy.settings.connection import db_connection_handler
from src.models.sqlalchemy.repositories.company_repository import CompanyRepository
from src.controllers.company.withdraw_controller import CompanyWithdrawController
from src.views.withdraw_view import WithdrawView

def company_withdraw_view_composer():
    repository = CompanyRepository(db_connection=db_connection_handler)
    controller = CompanyWithdrawController(company_repository=repository)
    view = WithdrawView(controller)

    return view
