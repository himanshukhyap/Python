from django.db import models

class Student(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
