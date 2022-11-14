from django.db import models

#using command python3 manage.py makemigrations and python3 manage.py migrate
# source venv/bin/activate
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

class Course(models.Model):
    courseName = models.CharField(max_length=50)
    coursePrice = models.IntegerField()
    duration = models.IntegerField()
    status = models.BooleanField(default = True)
    url = models.URLField()
    createdAt = models.DateTimeField(auto_now_add=True,null=True) 
    # auto_now_add is for creation time
    updateedAt = models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        db_table = "courses"

    # present data on admin side with name not object
    def __str__(self):
        return self.courseName 

class Student(Course):#inheritance the table
    #bad practice because we have only option for oneToOne relationship
    #in admin side, Foreign table can shows the value of both tables so we can not use this
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    password = models.CharField(max_length=20)
    class Meta:
        db_table = "students"
    def __str__(self):
        return self.courseName 

class Category(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default = True)    
    class Meta:
        db_table = "categories"
    def __str__(self):
        return self.name 

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default = True)    
    price = models.IntegerField()
    qty = models.IntegerField()
    class Meta:
        db_table = "products"
    def __str__(self):
        return self.name 