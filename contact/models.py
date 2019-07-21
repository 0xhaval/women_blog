from django.db import models

# Create your models here.
class contact(models.Model):
    Fname   = models.CharField(max_length=40)
    Lname   = models.CharField(max_length=40)
    Email   = models.EmailField()
    Massege = models.TextField()
