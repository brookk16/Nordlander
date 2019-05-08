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
    
    """
    THIS TEST SHOULD FAIL" status code should not be 404 (should be 200)
    """
    def test_that_should_fail(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        page = self.client.get("/")
        self.assertEqual(page.status_code, 404)
        self.assertTemplateUsed(page, "home.html")
    
    """
    Test that ensures the correct page is displayed when users go to their profile (to see their purchased features)
    """
    
    def test_correct_profile_page_is_loaded(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        page = self.client.get("/accounts/myFeatures/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "myFeatures.html")
        self.assertEqual()
        