from django.db import models
from django.utils import timezone

# Create your models here.
class Bugs(models.Model):
    
    STATUSES = {
        ("To do", "To do"),
        ("Doing", "Doing"),
        ("Fixed", "Fixed"),
    }
    
    BUG_TYPES = {
        ("Item", "Item"),
        ("World", "World"),
        ("Skills", "Skills"),
        ("Quests", "Quests"),
        ("Base game", "Base game")
    }
    
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    upvotes = models.IntegerField(default=0)
    status = models.CharField(choices=STATUSES, default="TODO", max_length=6)
    type = models.CharField(choices=BUG_TYPES, max_length=10, default="Base game")
    
    """comments = models.ForeignKey(Comment, null=False)"""
    
    

    def __str__(self):
        return self.name
