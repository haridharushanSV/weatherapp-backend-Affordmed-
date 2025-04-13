
from django.db import models

class data(models.Model):
    user=models.CharField(max_length=20)
    passw= models.CharField(max_length=20)
