from django.contrib import admin

from .models import CustomBotDataset


@admin.register(CustomBotDataset)
class CustomBotDatasetAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'answer', 'active']
