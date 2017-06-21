from django.contrib import admin
from .models import Number


@admin.register(Number)
class AdminClient(admin.ModelAdmin):
    list_display = ('phone_number', 'created')
    list_filter = ('phone_number', 'created')
