from sqlalchemy import Column, String, Numeric, BIGINT
from src.models.sqlalchemy.settings.base import Base

class CompanyTable(Base):
    __tablename__ = "company"

    id = Column(BIGINT, primary_key=True)
    revenue = Column(Numeric(precision=10, scale=2), nullable=False, default=0)
    age = Column(BIGINT, nullable=False)
    trade_name = Column(String(length=200), nullable=False)
    phone = Column(String(length=20), nullable=False)
    corporate_email = Column(String(length=60), nullable=False)
    category = Column(String(), nullable=False)
    balance = Column(Numeric(precision=10, scale=2), nullable=False, default=0)

def __repr__(self) -> str:
    return (
        f"Company [trade_name={self.trade_name}, "
        f"corporate_email={self.corporate_email}, "
        f"revenue={self.revenue}, "
        f"phone={self.phone}, "
        f"category={self.category}, "
        f"age={self.age}, "
        f"balance={self.balance}]"
    )
