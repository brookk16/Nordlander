from django.test import TestCase
from .forms import AddBugForm
from .models import Bugs
from django.contrib.auth import get_user_model
from .views import bug_info

User=get_user_model()

class TestAddBugForm(TestCase):
    """
    Tests the AddBugForm 
    """
    def test_AddBugForm_is_valid(self):
        form = AddBugForm({'name': 'Test', 'description': "this is a test description for a bug", "type": "Items"})
        self.assertTrue(form.is_valid())
    
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
    def test_all_bugs_page(self):
        page = self.client.get("/bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")
    
    """
    Tests that a test feature can be found, and the correct page rendered
    """
    def test_feature_info_page(self):
        bug = Bugs(name="test", description="test", status="To do")
        bug.save()
        
        page = self.client.get("/bugs/{0}/".format(bug.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugInfo.html")
    
        
       
        
   
        
        
        
        