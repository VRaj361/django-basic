from django.db import models

# Create your models here.
hobbies =(
    ('reading','Reading'),
    ('playing','Playing')
)

class User(models.Model):
    name = models.CharField(max_length=50)
    hobbies = models.CharField(max_length=50,choices= hobbies)
    age = models.IntegerField()
    email = models.EmailField(unique = True, null = False, max_length=254)
    class Meta:
        db_table = "users"

    def __str__(self):
        return self.name

class Netflix(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    class Meta:
        db_table = "netflix"

    def __str__(self):
        return self.name