from django.db import models

class Student(models.Model):
    roll = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name
