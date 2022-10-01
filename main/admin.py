from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.ImageWord)
class ImageWordAdmin(admin.ModelAdmin):
    list_display = ['label', 'url']