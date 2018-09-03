from django.db import models


# Create your models here.
class SignUp(models.Model):
    name = models.CharField()
    email = models.EmailField()
    body = models.CharField()

    def __str__(self):
        return self.name
