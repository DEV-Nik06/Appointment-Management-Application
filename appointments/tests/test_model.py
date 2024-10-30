
from django.test import TestCase
from appointments.models import Availability, Staff
from django.core.exceptions import ValidationError

class AvailabilityModelTest(TestCase):

    def setUp(self):
        # Set up a staff instance for the tests
        self.staff = Staff.objects.create(name="John Doe")

    def test_start_time_before_end_time(self):
        # Test to check if ValidationError is raised when start_time >= end_time
        availability = Availability(
            staff=self.staff,
            start_date='2024-10-01',
            end_date='2024-10-01',
            start_time='12:00',
            end_time='11:00',  # Invalid, end_time is before start_time
        )
        with self.assertRaises(ValidationError):
            availability.full_clean()  # This triggers the model's clean method for validation

    def test_valid_availability(self):
        availability = Availability(
            staff=self.staff,
            start_date='2024-10-01',
            end_date='2024-10-01',
            start_time='09:00',
            end_time='11:00',
        )
        try:
            availability.full_clean()  # This should pass without errors
        except ValidationError:
            self.fail("Availability raised ValidationError unexpectedly.")
