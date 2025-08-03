from src.models.sqlalchemy.settings.connection import db_connection_handler
from src.models.sqlalchemy.repositories.individual_repository import IndividualRepository
from src.controllers.individual.create_controller import IndividualCreateController
from src.views.create_view import CreateView

def individual_create_view_composer():
    repository = IndividualRepository(db_connection=db_connection_handler)
    controller = IndividualCreateController(individual_repository=repository)
    view = CreateView(controller)

    return view
