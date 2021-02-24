from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll_no','email','password']
