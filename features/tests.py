from django.test import TestCase
from .models import Features
from django.contrib.auth import get_user_model
from .views import all_features, feature_info

User=get_user_model()

class TestViews(TestCase):
    """
    Creates a user for the tests
    """
    def setUp(self):
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
    
    """
    Tests that the features page renders correctly
    """
    def test_all_features_page(self):
        page = self.client.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")
    
    """
    Tests that a test feature can be found, and the correct page rendered
    """
    def test_feature_info_page(self):
        feature = Features(name="test", description="test", status="To do", likes=0)
        feature.save()
        
        page = self.client.get("/features/{0}/".format(feature.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "featureInfo.html")
    

    
        
       
        
   