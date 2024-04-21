from fastapi import APIRouter

from schema.appointment import AppointmentsCreateEdit, appointments
from services.appointment import AppointmentService


appointment_router = APIRouter()


@appointment_router.get('', status_code=200)
def get_appointments():
    data = AppointmentService.parse_appointments(appointment_data=appointments)
    return {'message': 'Successful', 'data': data}


@appointment_router.get('/{appointment_id}', status_code=200)
def get_appointment_by_id(appointment_id: int):
    data = AppointmentService.get_appointment_by_id(appointment_id)
    return {'message': 'Successful', 'data': data}


@appointment_router.post('/{patient_id}', status_code=201)
def create_appointment(payload: AppointmentsCreateEdit):
    data = AppointmentService.create_appointment(payload)
    return {'message': 'Appointment Created Successfully', 'data': data}


@appointment_router.put('/{appointment_id}', status_code=200)
def edit_appointment(appointment_id: int, payload: AppointmentsCreateEdit):
    data = AppointmentService.edit_appointment(appointment_id, payload)
    return {'message': 'Appointment Updated Successful', 'data': data}


@appointment_router.put('/complete_appointment/{appointment_id}', status_code=200)
def complete_appointment(appointment_id: int):
    data = AppointmentService.complete_appointment(appointment_id)
    return {'message': 'Appointment Completed Successfully', 'data': data}


@appointment_router.delete('/{appointment_id}', status_code=200)
def delete_appointment(appointment_id: int):
    AppointmentService.delete_appointment(appointment_id)
    return {'message': 'Appointment deleted successfully'}
