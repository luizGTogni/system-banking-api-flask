from sqlalchemy.orm.exc import NoResultFound
from src.models.interfaces.customer import CustomerInterface
from src.models.interfaces.individual_repository import IndividualRepositoryInterface
from src.models.sqlalchemy.settings.connection import DBConnectionHandler
from src.models.sqlalchemy.entities.individual import IndividualTable

class IndividualRepository(CustomerInterface, IndividualRepositoryInterface):
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def generate_report(self) -> None:
        pass

    def withdraw(self, value: float) -> None:
        pass

    def create(
            self,
            full_name: str,
            age: int,
            phone: str,
            email: str,
            category: str,
            monthly_income: float,
        ) -> None:
        with self.__db_connection as db:
            try:
                individual_data = IndividualTable(
                    monthly_income = monthly_income,
                    age = age,
                    full_name = full_name,
                    phone = phone,
                    email = email,
                    category = category,
                    balance = 0
                )

                db.session.add(individual_data)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def list_all(self) -> list[IndividualTable]:
        with self.__db_connection as db:
            try:
                users = db.session.query(IndividualTable).all()
                return users
            except NoResultFound:
                return []
