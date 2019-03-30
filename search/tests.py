from django.test import TestCase
from .views import do_search
from featuresAndBugs.models import FeaturesAndBugs

# Create your tests here.
class SearchTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_str(self):
        search_name = FeaturesAndBugs(name='test')
        self.assertEqual(str(search_name), 'test')
