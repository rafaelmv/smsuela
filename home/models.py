from django.db import models

# Create your models here.
class User(models.Model):
    phone_number = models.CharField(max_length=12)
    created = models.DateTimeField('date created')