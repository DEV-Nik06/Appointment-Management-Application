from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Appointment , Staff ,Availability




class UserRegistrationForm(forms.ModelForm):
    role = forms.ChoiceField(choices=[('student', 'Student'), ('staff', 'Staff')], required=True)
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(),
        required=True
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

        
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)






class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Select a date'}),
        required=True,
        error_messages={'required': 'Please choose an appointment date.'},
        help_text='Select a date for your appointment.'
    )
    appointment_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'placeholder': 'Select time'}),
        required=True,
        error_messages={'required': 'Please specify an appointment time.'}
    )
    staff = forms.ModelChoiceField(
        queryset=Staff.objects.all(),
        empty_label="Select Staff",
        error_messages={'required': 'Please select a staff member.'}
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Provide details about your appointment', 'rows': 3})
    )

    

    class Meta:
        model = Appointment
        fields = ['appointment_date', 'appointment_time', 'staff', 'description']

    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic here if needed
        return cleaned_data




 # Make sure to import your Availability model


class StaffAvailabilityForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
    )
    start_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        required=True,
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        required=True,
    )
    available_days = forms.MultipleChoiceField(
        choices=[
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False  # Optional, depending on your logic
    )

    class Meta:
        model = Availability
        fields = ['start_date', 'end_date', 'start_time', 'end_time', 'available_days']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # Ensure that the start time is before the end time
        if start_time and end_time:
            if start_time >= end_time:
                self.add_error('end_time', "End time must be after start time.")

        # Ensure that the start date is before the end date
        if start_date and end_date:
            if start_date > end_date:
                self.add_error('end_date', "End date must be after or equal to the start date.")

        return cleaned_data


