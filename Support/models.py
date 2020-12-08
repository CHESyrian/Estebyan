from django.db import models
from django.contrib.auth.models import User


class Contacts(models.Model):
    UserName = models.ForeignKey(User, on_delete=models.CASCADE)
    Email    = models.EmailField()
    Title    = models.CharField(max_length=120, default='no title')
    Subject  = models.CharField(max_length=12000, null=True)
    Con_Date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.UserName.username


class Reports(models.Model):
    UserName = models.ForeignKey(User, on_delete=models.CASCADE)
    Title    = models.CharField(max_length=120, default='no title')
    Subject  = models.CharField(max_length=12000, null=True)
    Rep_Date = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.UserName.username
