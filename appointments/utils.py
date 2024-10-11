# # utils.py
# from .models import Appointment

# def create_appointment(student, staff, appointment_date, time, description=''):
#     if Appointment.objects.filter(
#         student=student,
#         staff=staff,
#         appointment_date=appointment_date,
#         time=time
#     ).exists():
#         print("This appointment already exists.")
#         return None
#     else:
#         appointment = Appointment.objects.create(
#             student=student,
#             staff=staff,
#             appointment_date=appointment_date,
#             time=time,
#             description=description
#         )
#         print("Appointment created successfully.")
#         return appointment
