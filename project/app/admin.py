
from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_name', 'stu_address', 'stu_mobile')
admin.site.register(Student,StudentAdmin)