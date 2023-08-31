from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    college = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    aadhar = models.CharField(max_length=100)

    def __str__(self):
        return self.name
