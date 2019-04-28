from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Bugs(models.Model):
    
    STATUSES = {
        ("To do", "To do"),
        ("Doing", "Doing"),
        ("Fixed", "Fixed"),
    }
    
    BUG_TYPES = {
        ("Items", "Items"),
        ("Worlds", "Worlds"),
        ("Skills", "Skills"),
        ("Quests", "Quests"),
        ("Base game", "Base game")
    }
    
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    created_date = models.DateField(default=datetime.now)
    upvotes = models.IntegerField(default=0)
    status = models.CharField(choices=STATUSES, default="To do", max_length=6)
    type = models.CharField(choices=BUG_TYPES, max_length=10, default="Base game")
    user_upvoted = models.ManyToManyField(User)
    
    
    

    def __str__(self):
        return self.name
