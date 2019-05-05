from django.test import TestCase
import json

# Create your tests here.
class TestViews(TestCase):
    
    def test_get_graph_page(self):
        """
        Test to see if performance page is returned
        """
        page = self.client.get("/performance/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "performance.html")
        
    def test_to_see_ajax_request(self):
        """
        Test to see if ajax view returns correct data (the test database alos needs to be filled before testing)
        """
        response = self.client.post('/performance/api/data/', content_type='application/json')
        json_string = response.content
        json_string = response.content
        response_data = json.loads(str(response.content, encoding='utf8'))
        self.assertEquals(response_data["labels2"], ["To do", "Doing", "Fixed"])