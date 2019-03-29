from django.db import models

# Create your models here.
class FeaturesAndBugs(models.Model):
    
    STATUSES = (
        ("TO DO", "To do"),
        ("DOING", "Doing"),
        ("DONE", "Done")
        )
    TYPES = (
        ("BUG", "Bug"),
        ("FEATURE", "Feature")
        )
    
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    comments = models.TextField()
    status = models.CharField(choices=STATUSES, default="TO DO", max_length=5)
    type = models.CharField(choices=TYPES, max_length=20)
    upvotes = models.IntegerField() 
    group = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
