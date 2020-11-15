from django.contrib.auth.models import User
from django.db import models


class Profiles(models.Model):
    UserName  = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_User   = models.CharField(primary_key=True, max_length=12, unique=True)
    FirstName = models.CharField(max_length=32, null=True)
    LastName  = models.CharField(max_length=32, null=True)
    Birthdate = models.DateField(null=True)
    Qu_Shares = models.IntegerField(default=0)
    Questionnais = models.IntegerField(default=0)
    def __str__(self):
        return self.UserName.username
