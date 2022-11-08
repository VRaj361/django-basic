from django.db import models

#using command python3 manage.py makemigrations and python3 manage.py migrate
# sourse venv/bin/activate
# Create your models here.
class Employee(models.Model):


    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    isActivate = models.BooleanField(default=True)
    password = models.CharField(max_length=20)
    address = models.TextField()
    salary = models.FloatField(null=True)
    mobile = models.BigIntegerField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True,null=True) 
    # auto_now_add is for creation time
    updateedAt = models.DateTimeField(auto_now=True,null=True)
    # auto now is for updation time
    birthdate = models.DateField(null=True)
    birthtime = models.TimeField(null=True)
    # table name
    class Meta:
        db_table = "employees"

    # present data on admin side with name not object
    def __str__(self):
        return self.name 