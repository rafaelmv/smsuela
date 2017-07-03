from django.contrib import admin
from .models import Number, Message


@admin.register(Number)
class AdminClient(admin.ModelAdmin):
    list_display = ('phone_number', 'created_at')
    list_filter = ('phone_number', 'created_at')

@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = ('text_message', 'created_at')
    list_filter = ('text_message', 'created_at')
