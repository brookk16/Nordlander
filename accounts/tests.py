from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class TestViews(TestCase):
    """
    Test that creates a user and logs them in.
    """
        
    def test_login_and_user_creation(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home.html")