from django.db import models
from django.contrib.auth.models import User


class Questionnaires(models.Model):
    UserName = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Qs_Title = models.CharField(max_length=120, null=True)
    Qs_Name  = models.CharField(max_length=160, null=True)
    Qs_Path  = models.CharField(max_length=320, null=True)
    Qs_Date  = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.UserName.username
