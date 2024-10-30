# from django.test import TestCase

# Create your tests here.
from django.test import TestCase

class SimpleTest(TestCase):
    def test_simple_math(self):
        self.assertEqual(1 + 1, 2)
