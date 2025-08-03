from sqlalchemy.orm.exc import NoResultFound
from src.models.interfaces.customer import CustomerInterface
from src.models.sqlalchemy.settings.connection import DBConnectionHandler
from src.models.sqlalchemy.entities.individual import IndividualTable

class IndividualRepository(CustomerInterface):
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def create(
            self,
            name: str,
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
                    full_name = name,
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
                customers = db.session.query(IndividualTable).all()
                return customers
            except NoResultFound:
                return []

    def generate_report(self, customer_id: int) -> None:
        with self.__db_connection as db:
            try:
                customer = db.session.query(IndividualTable).filter_by(id=customer_id).first()
                return {
                    "name": customer.full_name,
                    "category": customer.category,
                    "balance": customer.balance
                }
            except NoResultFound:
                return {}

    def withdraw(self, customer_id: int, value: float) -> bool:
        with self.__db_connection as db:
            try:
                limit = 500.0
                customer = db.session.query(IndividualTable).filter_by(id=customer_id).first()

                if value <= customer.balance and value <= limit:
                    customer.balance -= value
                    db.session.commit()
                    return True

                return False
            except Exception as exception:
                db.session.rollback()
                raise exception
