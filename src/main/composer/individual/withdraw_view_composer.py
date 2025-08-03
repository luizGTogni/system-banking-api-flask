from src.models.sqlalchemy.settings.connection import db_connection_handler
from src.models.sqlalchemy.repositories.individual_repository import IndividualRepository
from src.controllers.individual.withdraw_controller import IndividualWithdrawController
from src.views.withdraw_view import WithdrawView

def individual_withdraw_view_composer():
    repository = IndividualRepository(db_connection=db_connection_handler)
    controller = IndividualWithdrawController(individual_repository=repository)
    view = WithdrawView(controller)

    return view
