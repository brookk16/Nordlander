from django.test import TestCase
from .models import FeaturesAndBugs

# Create your tests here.
class FeaturesAndBugsTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        test_name = FeaturesAndBugs(name='A product')
        self.assertEqual(str(test_name), 'A product')
