from django.db import models

# Create your models here.
class book(models.Model):
    Firstname=models.CharField(max_length=200)
    Lastname=models.CharField(max_length=200)
    Carname=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    State=models.CharField(max_length=200)
    Zip=models.CharField(max_length=200,)

