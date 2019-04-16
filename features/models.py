from django.db import models

# Create your models here.
class Features(models.Model):
    
    FEATURE_TYPES = {
        ("ITEM", "Item"),
        ("WORLD", "World"),
        ("SKILLS", "Skills"),
        ("QUESTS", "Quests")
    }
    
    STATUSES = {
        ("TODO", "To do"),
        ("DOING", "Doing"),
        ("AVAILABLE", "Available"),
    }
    
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    type = models.CharField(choices=FEATURE_TYPES, max_length=6, default="ITEM")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    image_carousel1 = models.ImageField(upload_to='images', default="Photo not available")
    image_carousel2 = models.ImageField(upload_to='images', default="Photo not available")
    image_carousel3 = models.ImageField(upload_to='images', default="Photo not available")
    
    likes =  models.IntegerField(default=0)
    status = models.CharField(choices=STATUSES, default="TODO", max_length=14)

    def __str__(self):
        return self.name
