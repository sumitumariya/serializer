
from django.db import models

# Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_address = models.CharField(max_length=80)
    stu_mobile = models.IntegerField()