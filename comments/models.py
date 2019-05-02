from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from bugs.models import Bugs



# Create your models here.

class Comments(models.Model):
    
    username = models.CharField(max_length=30,default=User )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bug_id = models.ForeignKey(Bugs, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    created_date =  models.DateField(default=datetime.now)
    
    
    def __str__(self):
        return self.username
        

