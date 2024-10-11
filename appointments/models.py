from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name







class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
        ('completed', 'Completed'),
    ]
    
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, related_name='staff_appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        unique_together = (('student', 'staff', 'appointment_date', 'appointment_time'),)

    def __str__(self):
        return f"Appointment with {self.staff} for {self.student} on {self.appointment_date} at {self.appointment_time}"

    def clean(self):
        # Ensure the appointment date is in the future
        # if self.appointment_date < timezone.now().date():
        #     raise ValidationError('Appointment date cannot be in the past.')
        
        # Combine appointment_date and appointment_time to create a datetime object
        appointment_datetime = timezone.make_aware(
            timezone.datetime.combine(self.appointment_date, self.appointment_time)
        )
        
        # Ensure the appointment time is in the future
        if appointment_datetime <= timezone.now():
            raise ValidationError('Appointment time cannot be in the past.')





class Availability(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)
    available_date = models.DateField()  # Specific date availability
    start_time = models.TimeField()
    end_time = models.TimeField()
    available_days = models.CharField(max_length=255, blank=True, null=True)  # Storing available days as a string

    class Meta:
        unique_together = (('staff', 'available_date', 'start_time', 'end_time'),)

    def __str__(self):
        return f"{self.staff} is available on {self.available_date} from {self.start_time} to {self.end_time}"

    def clean(self):
        # Check that end_time is after start_time
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after start time.")

