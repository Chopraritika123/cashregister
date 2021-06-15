from django.db import models

# Create your models here.

class Hill(models.Model):
    def __str__(self) -> str:
        return self.amount
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    remarks=models.CharField(blank=True, max_length=100)
    amount= models.CharField(blank=True, max_length=100)
    sign=models.CharField(blank=True, max_length=1) 
