from pydantic import BaseModel, constr
from typing import Optional

class EmployeeCreate(BaseModel):
    name: str
    mobile_no: constr(min_length=10, max_length=10)
    employee_id_no: str
    aadhaar_no: constr(min_length=12, max_length=12)
    pan_no: constr(min_length=10, max_length=10)
    address: Optional[str]
    email: Optional[str]

class EmployeeOut(BaseModel):
    id: int
    name: str
    mobile_no: str
    employee_id_no: str
    aadhaar_no: str
    pan_no: str
    address: Optional[str]
    email: Optional[str]

    class Config:
        orm_mode = True

