from django.db import models

# Create your models here.
class PersonDate(models.Model):
   first_name=models.CharField(max_length=50,blank=True)
   last_name=models.CharField(max_length=50,blank=True)
   city=models.CharField(max_length=50,blank=True)
   country=models.CharField(max_length=50,blank=True)
   index = models.CharField(max_length=10, blank=True)

