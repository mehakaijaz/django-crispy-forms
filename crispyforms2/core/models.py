from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    
    class Subjects(models.IntegerChoices):
        webd=1
        compscience=2
        datascience=3
    subjects=models.PositiveSmallIntegerField(choices=Subjects.choices)
    date_of_birth=models.DateField()