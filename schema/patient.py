from typing import Optional
from pydantic import BaseModel


# patient pydantic definition
class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str


# pydantic definition Creating patient data
class PatientsCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str


# pydantic definition for updating patient data
class PatientsEdit(BaseModel):
    name: Optional[str]=None
    age: Optional[int] = None
    sex: Optional[str] = None
    weight: Optional[float]=None
    height: Optional[float]=None
    phone: Optional[str] = None
    

patients: dict[int, Patients] = {
    0: Patients(
        id=0, name='Chris Ebulem', age=27, sex= 'male', weight=81.5, height=58.5, phone= '08120752396'
	),
    1: Patients(
        id=1, name='Eche Jane', age=35, sex= 'female', weight=89.0, height=61.8, phone= '08139449621'
	),
    2: Patients(
        id=2, name='Cillia Chase', age=25, sex= 'female', weight=75.5, height=68, phone= '07034558810'
	)
}