from django.db import models

# Create your models here.
class Number(models.Model):
    phone_number = models.CharField(max_length=12)
    created = models.DateTimeField('date created')
