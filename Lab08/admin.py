from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Post)
class CreatePosr(admin.ModelAdmin):
    list_display=['id','name','content']

