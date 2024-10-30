from django.test import TestCase
from django.urls import reverse
from appointments.models import Staff, Availability
from django.contrib.auth.models import User

class ManageAvailabilityViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.staff = Staff.objects.create(user=self.user)
        self.client.login(username='testuser', password='12345')  # Log the user in

    def test_get_manage_availability_view(self):
        response = self.client.get(reverse('manage_availability_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointments/manage_availability.html')

    def test_post_valid_availability(self):
        data = {
            'start_date': '2024-10-01',
            'end_date': '2024-10-01',
            'start_time': '09:00',
            'end_time': '11:00',
            'available_days': ['Monday', 'Wednesday'],
        }
        response = self.client.post(reverse('manage_availability_view'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Availability.objects.filter(staff=self.staff).exists())
