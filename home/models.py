from django.db import models

# Create your models here.
class Number(models.Model):
    phone_number = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
