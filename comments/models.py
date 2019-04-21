from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from bugs.models import Bugs



# Create your models here.

class Comments(models.Model):
    
    
    username = models.CharField(max_length=30,default="Anon" )
    user_id = models.ManyToManyField(User)
    bug_id = models.ForeignKey(Bugs, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    
    
    

    def __str__(self):
        return self.username
        

