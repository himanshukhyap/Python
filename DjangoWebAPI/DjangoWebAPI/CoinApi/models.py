# Create your models here.
from django.db import models

class AssestManager(models.Model):
    AssestId = models.CharField(max_length=250, blank=False)
    Symbol = models.CharField(blank=True ,max_length=250)
    Name = models.CharField(blank=True ,max_length=250)
    ThumbImage = models.CharField(blank=True ,max_length=250)
    SmallImage = models.CharField(blank=True,max_length=250 )
    LargeImage = models.CharField(blank=True,max_length=250 )
  


