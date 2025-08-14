from sqlalchemy import Column, Integer, String, Date, DECIMAL
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, index=True)  # Custom ID like EMP001
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    mobile_number = Column(String, unique=True, nullable=False)
    email = Column
