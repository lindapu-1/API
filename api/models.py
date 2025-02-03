from django.db import models

# Create your models here.
class SustainabilityAction(models.Model):#like a table in a database
    action = models.CharField(max_length=255)#Recycling
    date = models.DateField(auto_now_add=True)#2025-01-01
    points = models.IntegerField()#100

    def __str__(self):
        return self.action
    

