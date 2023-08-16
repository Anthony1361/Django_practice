from django.db import models

# Create your models here.

class Person(models.Model):
    firstName = models.CharField(max_length=5)
    lastName = models.CharField(max_length=5)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.firstName




