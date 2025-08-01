from sqlalchemy import Column, String, DECIMAL, BIGINT
from src.models.sqlalchemy.settings.base import Base

class IndividualTable(Base):
    __tablename__ = "individual"

    id = Column(BIGINT, primary_key=True)
    monthly_income = Column(DECIMAL, nullable=False, default=0)
    age = Column(BIGINT, nullable=False)
    full_name = Column(String(length=200), nullable=False)
    phone = Column(String(length=20), nullable=False)
    email = Column(String(length=60), nullable=False)
    category = Column(String(), nullable=False)
    balance = Column(DECIMAL, nullable=False, default=0)

def __repr__(self) -> str:
    return (
        f"Individual [full_name={self.full_name}, "
        f"email={self.email}, "
        f"balance={self.balance}, "
        f"phone={self.phone}, "
        f"category={self.category}, "
        f"age={self.age}, "
        f"monthly_income={self.monthly_income}]"
    )
