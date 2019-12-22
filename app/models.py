from django.db import models

# Create your models here.
class employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    dob=models.DateField()
    email=models.EmailField(max_length=32)
    password=models.CharField(max_length=22)
    mobileno=models.CharField(max_length=10)
    salary=models.CharField(max_length=32)
