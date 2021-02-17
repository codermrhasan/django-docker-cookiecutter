from django.contrib import admin
from django.db import models
from django.db.models.base import Model

from .models import Food

class FoodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Food, FoodAdmin)
