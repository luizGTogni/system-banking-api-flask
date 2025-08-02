from sqlalchemy.orm.exc import NoResultFound
from src.models.interfaces.customer import CustomerInterface
from src.models.sqlalchemy.settings.connection import DBConnectionHandler
from src.models.sqlalchemy.entities.company import CompanyTable

class CompanyRepository(CustomerInterface):
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def create(
            self,
            name: str,
            age: int,
            phone: str,
            email: str,
            category: str,
            revenue: float,
        ) -> None:
        with self.__db_connection as db:
            try:
                company_data = CompanyTable(
                    revenue = revenue,
                    age = age,
                    trade_name = name,
                    phone = phone,
                    corporate_email = email,
                    category = category,
                    balance = 0
                )

                db.session.add(company_data)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def list_all(self) -> list[CompanyTable]:
        with self.__db_connection as db:
            try:
                customers = db.session.query(CompanyTable).all()
                return customers
            except NoResultFound:
                return []

    def generate_report(self, customer_id: int) -> dict:
        with self.__db_connection as db:
            try:
                customer = db.session.query(CompanyTable).filter_by(id=customer_id).first()
                return {
                    "name": customer.trade_name,
                    "category": customer.category,
                    "balance": customer.balance
                }
            except NoResultFound:
                return {}

    def withdraw(self, customer_id: int, value: float) -> bool:
        with self.__db_connection as db:
            try:
                limit = 1000.0
                customer = db.session.query(CompanyTable).filter_by(id=customer_id).first()

                if value <= customer.balance and value <= limit:
                    customer.balance -= value
                    db.session.commit()
                    return True

                return False
            except Exception as exception:
                db.session.rollback()
                raise exception
