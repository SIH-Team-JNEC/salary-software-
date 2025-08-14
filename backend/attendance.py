from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, date
from typing import List, Optional
from database import SessionLocal
from models import Employee
from sqlalchemy import Column, Integer, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from pydantic import BaseModel

# ---------------- Attendance Model ----------------
class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    work_date = Column(Date, nullable=False)
    clock_in = Column(DateTime, nullable=False)
    clock_out = Column(DateTime, nullable=True)

    employee = relationship("Employee")  # Li
