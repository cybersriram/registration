from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=40)
    mail= models.CharField(max_length=40)
    title = models.CharField(max_length=5)
    clgname = models.CharField(max_length=40)
    dept = models.CharField(max_length=30)
