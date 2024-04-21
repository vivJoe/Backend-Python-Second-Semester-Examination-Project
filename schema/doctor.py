from enum import Enum
from typing import Optional
from pydantic import BaseModel


# Doctor Pydantic definition
class Doctors(BaseModel):
     id: int
     name: str
     specialization: str
     phone: str
     is_available: bool = True


# pydantic definition for Creating Doctor data
class DoctorsCreate(BaseModel):
     name: str
     specialization: str
     phone: str

     
# pydantic definition for Updating Doctor data
class DoctorsEdit(BaseModel):
     name: Optional[str] = None
     specialization: Optional[str] = None
     phone: Optional[str] = None
     

doctors: dict[int, Doctors] = {
     0: Doctors(id=0, name='Dr. Vivian Oba', specialization='Dentist', phone='07066091382', is_available=False),
     1: Doctors(id=1, name='Dr. Jonathan Iwegbu', specialization='Dermatologist', phone='08076039813'),
     2: Doctors(id=2, name='Dr. Nweke Rita', specialization='Surgeon', phone='08054571943')

}