from django.shortcuts import render, redirect,get_object_or_404
from appointments.models import Appointment,Staff,Availability
from django.contrib import messages
from appointments.forms import AppointmentForm,StaffAvailabilityForm
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone

# home



def home_view(request):
    
        return render(request, 'home.html')
    




# book_appointment


@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment_date = form.cleaned_data['appointment_date']
            appointment_time = form.cleaned_data['appointment_time']
            staff_member = form.cleaned_data['staff']

            # Check for existing appointment
            if Appointment.objects.filter(
                student=request.user,
                staff=staff_member,
                appointment_date=appointment_date,
                appointment_time=appointment_time
            ).exists():
                form.add_error(None, 'An appointment with this staff member at the selected date and time already exists.')
            else:
                # Check if the staff member has set their availability
                availability = Availability.objects.filter(
                  staff=staff_member,
                start_date__lte=appointment_date,
                end_date__gte=appointment_date,
                start_time__lte=appointment_time,
                end_time__gte=appointment_time
                ).exists()

                if availability:
                    # If availability is set, check if the staff is available
                    if not availability:
                        form.add_error(None, "The selected staff is not available at the chosen time.")
                else:
                    # If no availability is set, allow booking anyway and mark it as pending
                    messages.warning(request, f"No availability set for {staff_member.user.username}. The appointment will be marked as pending until the staff updates their availability.")

                # Create the appointment if it does not exist
                appointment = form.save(commit=False)
                appointment.student = request.user  # Assign the logged-in user as the student
                appointment.status = 'pending'  # Mark as pending if no availability is set
                appointment.save()  # Now save the instance

                return redirect('view_appointments')
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})



# dashboard_view


import logging

logger = logging.getLogger(__name__)

@login_required
def dashboard_view(request):
    if request.user.groups.filter(name='Staff').exists():
        logger.info(f'{request.user} accessed the staff dashboard.')
        return render(request, 'staff_dashboard.html')
    elif request.user.groups.filter(name='Student').exists():
        logger.info(f'{request.user} accessed the student dashboard.')
        return render(request, 'student_dashboard.html')
   
    else:
        logger.info(f'{request.user} accessed the default dashboard.')
        return render(request, 'home.html')
    
# manage_appointments_view 




@login_required
def manage_availability_view(request):
    if request.method == 'POST':
        form = StaffAvailabilityForm(request.POST)
        if form.is_valid():
            # Create a new Availability instance
            availability = form.save(commit=False)
            availability.staff = request.user.staff  # Assuming user is related to Staff model

            # Ensure start_time, end_time, start_date, and end_date are not None
            if availability.start_time and availability.end_time and availability.start_date and availability.end_date:
                # Check for overlapping availability slots
                if Availability.objects.filter(
                    staff=availability.staff,
                    start_date__lte=availability.end_date,
                    end_date__gte=availability.start_date,
                    start_time__lt=availability.end_time,  # Correct time comparison
                    end_time__gt=availability.start_time   # Correct time comparison
                ).exists():
                    messages.error(request, "Availability for this date and time range already exists.")
                else:
                    availability.save()  # Save the instance
                    messages.success(request, "Your availability has been updated successfully.")
                    return redirect('manage_availability_view')  # Stay on the same page after submission
            else:
                messages.error(request, "Start date, end date, start time, and end time are required.")
    else:
        form = StaffAvailabilityForm()

    # Fetch current availabilities for the logged-in staff member
    availabilities = Availability.objects.filter(staff=request.user.staff)
    
    # Convert available_days from a stored string to a list (if applicable)
    for availability in availabilities:
        if isinstance(availability.available_days, str):
            availability.available_days = availability.available_days.strip('[]').replace("'", "").split(', ')

    return render(request, 'manage_availability.html', {'form': form, 'availabilities': availabilities})



# New view to handle deleting availability
@login_required
def delete_availability(request, availability_id):
    availability = get_object_or_404(Availability, id=availability_id, staff=request.user.staff)
    availability.delete()
    messages.success(request, "Availability slot deleted successfully.")
    return redirect('manage_availability_view')




# view_appointments



@login_required
def view_appointments(request):
    if request.user.is_staff:
        try:
            # Get the staff object for the logged-in user
            staff = Staff.objects.get(user=request.user)
            # Fetch appointments where the logged-in staff is assigned
            appointments = Appointment.objects.filter(staff=staff)
        except Staff.DoesNotExist:
            appointments = []  # Handle case where the staff object doesn't exist
    else:
        # For students, fetch their appointments
        appointments = Appointment.objects.filter(student=request.user)

    has_appointments = appointments.exists()  # Check if there are any appointments

    return render(request, 'view_appointments.html', {'appointments': appointments, 'has_appointments': has_appointments})






@login_required
def confirm_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.user.is_staff:  # Check if the user is staff
        appointment.status = 'confirmed'
        appointment.save()
        return redirect('view_appointments')  # Redirect to appointments view
    else:
        # Optionally handle the case where a non-staff user tries to confirm an appointment
        return redirect('view_appointments')

@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.user.is_staff:  # Check if the user is staff
        appointment.status = 'Canceled'
        appointment.save()
        return redirect('view_appointments')  # Redirect to appointments view
    else:
        # Optionally handle the case where a non-staff user tries to confirm an appointment
        return redirect('view_appointments')
    

@login_required
def delete_appointment(request, appointment_id):
    if request.user.is_staff:
        appointment = get_object_or_404(Appointment, id=appointment_id, staff__user=request.user)
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully.')
        return redirect('view_appointments')
    else:
        messages.error(request, 'You do not have permission to delete this appointment.')
        return redirect('view_appointments')
    

# About

def about_view(request):
    return render(request, 'about.html')