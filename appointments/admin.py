from django.contrib import admin
from .models import Appointment, Staff

# Admin for Appointment model
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'staff', 'appointment_date', 'appointment_time', 'description')   # Adjust based on actual model fields

# Admin for Staff model
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')  # Adjust based on actual model fields
    search_fields = ('name', 'email')

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Staff, StaffAdmin)
