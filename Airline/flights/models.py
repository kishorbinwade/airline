from django.db import models

# Create your models here.
from django.db import models

# Create your models here.  

class Airport(models.Model):
    city=models.CharField(max_length=32)
    code=models.CharField(max_length=32)

    def __str__(self):
        return f"{self.city} {self.code}"


class Flight(models.Model):
    origin=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure')
    destination=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='Arrivals')
    duration=models.IntegerField()
    
    def __str__(self):                      #For string representaion of flight DB
        return f"{self.id}:{self.origin} To {self.destination} Time {self.duration}"


class Passenger(models.Model):
    First_Name=models.CharField(max_length=64)
    Last_Name=models.CharField(max_length=64)
    flights=models.ManyToManyField(Flight,blank=True,related_name="passengers")

    def __str__(self): 
        return f"{self.First_Name} {self.Last_Name}"
        