from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Employee
from schemas import EmployeeCreate, EmployeeOut
from typing import List

router = APIRouter()

# Create employee
@router.post("/", response_model=EmployeeOut)
def create_employee(employee: EmployeeCreate):
    db: Session = SessionLocal()
    try:
        existing = db.query(Employee).filter(
            (Employee.employee_id_no == employee.employee_id_no) |
            (Employee.aadhaar_no == employee.aadhaar_no) |
            (Employee.pan_no == employee.pan_no)
        ).first()
        if existing:
            raise HTTPException(status_code=400, detail="Employee already exists")

        new_emp = Employee(**employee.dict())
        db.add(new_emp)
        db.commit()
        db.refresh(new_emp)
        return new_emp
    finally:
        db.close()

# Get all employees
@router.get("/", response_model=List[EmployeeOut])
def list_employees():
    db: Session = SessionLocal()
    try:
        return db.query(Employee).all()
    finally:
        db.close()

# Get single employee
@router.get("/{emp_id}", response_model=EmployeeOut)
def get_employee(emp_id: int):
    db: Session = SessionLocal()
    try:
        emp = db.query(Employee).get(emp_id)
        if not emp:
            raise HTTPException(status_code=404, detail="Employee not found")
        return emp
    finally:
        db.close()

# Delete employee
@router.delete("/{emp_id}")
def delete_employee(emp_id: int):
    db: Session = SessionLocal()
    try:
        emp = db.query(Employee).get(emp_id)
        if not emp:
            raise HTTPException(status_code=404, detail="Employee not found")
        db.delete(emp)
        db.commit()
        return {"message": "Employee deleted"}
    finally:
        db.close()
