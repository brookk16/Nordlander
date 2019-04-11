from django.db import models
from django.utils import timezone

# Create your models here.
class Bugs(models.Model):
    
    STATUSES = {
        ("TODO", "To do"),
        ("DOING", "Doing"),
        ("FIXED", "Fixed!"),
    }
    
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    upvotes = models.IntegerField(default=0)
    status = models.CharField(choices=STATUSES, default="TODO", max_length=6)
    
    """comments = models.ForeignKey(Comment, null=False)"""
    
    

    def __str__(self):
        return self.name
