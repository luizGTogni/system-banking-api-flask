from src.models.sqlalchemy.settings.connection import db_connection_handler
from src.models.sqlalchemy.repositories.individual_repository import IndividualRepository
from src.controllers.individual.list_all_controller import IndividualListAllController
from src.views.list_all_view import ListAllView

def individual_list_all_view_composer():
    repository = IndividualRepository(db_connection=db_connection_handler)
    controller = IndividualListAllController(individual_repository=repository)
    view = ListAllView(controller)

    return view
