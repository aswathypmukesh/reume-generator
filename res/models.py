from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email_id = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    edu = models.CharField(max_length=1000)
    exp = models.CharField(max_length=1000)
    skill1 = models.CharField(max_length=100)
    skill2 = models.CharField(max_length=100)
    skill3 = models.CharField(max_length=100)
    skill4 = models.CharField(max_length=100)