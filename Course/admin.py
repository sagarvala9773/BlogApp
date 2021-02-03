from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Student)
class ModelStudent(admin.ModelAdmin):
    list_display=['id','name','age',]

