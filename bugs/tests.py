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
    

    
        
       
        
   
        
        
        
        