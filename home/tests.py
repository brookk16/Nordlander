from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

User=get_user_model()

class TestViews(TestCase):
    """
    Creates a user for the tests
    """
    def setUp(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
    
    """
    Tests that the bugs page renders correctly
    """
    def test_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home.html")