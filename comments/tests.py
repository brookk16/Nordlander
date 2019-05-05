from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comments
from bugs.models import Bugs



class TestViews(TestCase):
    
    def test_add_comment(self):
        """
        Test to see if a comment is added to a bug, the comment will have that bug as it's bug_id. Also asserts that the user who added the comment, and the use_id are the same
        """
        user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')
        
        bug = Bugs(name="test", description="test", status="To do")
        bug.save()
        
        comment = Comments(comment ="test", bug_id = bug, user_id = user)
        comment.save()
        
        self.client.post("/comment/{0}/".format(bug.id))
        
        
        self.assertEqual(bug, comment.bug_id)
        self.assertEqual(user, comment.user_id)
      