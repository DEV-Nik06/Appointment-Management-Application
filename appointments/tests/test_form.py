from django.test import TestCase
from appointments.forms import StaffAvailabilityForm

class StaffAvailabilityFormTest(TestCase):

    def test_valid_form(self):
        data = {
            'start_date': '2024-10-01',
            'end_date': '2024-10-01',
            'start_time': '09:00',
            'end_time': '11:00',
            'available_days': ['Monday', 'Tuesday'],
        }
        form = StaffAvailabilityForm(data=data)
        self.assertTrue(form.is_valid())  # The form should be valid

    def test_invalid_form_end_time_before_start_time(self):
        data = {
            'start_date': '2024-10-01',
            'end_date': '2024-10-01',
            'start_time': '12:00',
            'end_time': '11:00',  # Invalid data
        }
        form = StaffAvailabilityForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('end_time', form.errors)  # Ensure 'end_time' error is raised
