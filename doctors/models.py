from django.db import models

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)  
    specialty = models.CharField(max_length=100)  
    time = models.TimeField()  
    day_of_week = models.CharField(max_length=9)
