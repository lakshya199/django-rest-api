from django.db import models

# Create your models here.
# class StreamPlatform(models.Model):
#     rating = models.IntegerField(default=0)
#     Directorname = models.CharField(max_length=150)
#     website = models.URLField(max_length=100)

#     def __str__(self):
#         return self.rating

class Movie(models.Model):
    
    name = models.CharField(max_length=30)
    Description = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

   
    def __str__(self):
        return self.name