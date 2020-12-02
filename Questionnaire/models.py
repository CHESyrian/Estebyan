from django.db import models
from django.contrib.auth.models import User


class Questionnaires(models.Model):
    UserName = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Qs_Title = models.CharField(max_length=120, null=True)
    Qs_Name  = models.CharField(max_length=160, null=True, unique=True)
    Qs_Path  = models.CharField(max_length=320, null=True)
    Qs_Dcrb  = models.CharField(max_length=320, default='No Describtion')
    Qs_Date  = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.UserName.username


class Qs_Shares(models.Model):
    Questionnaire = models.OneToOneField(Questionnaires, on_delete=models.CASCADE, primary_key=True)
    Shares_Num    = models.IntegerField(default=0)

    def __str__(self):
        return self.UserName.username


class Shares(models.Model):
    UserName      = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Questionnaire = models.ForeignKey(Questionnaires, on_delete=models.CASCADE, null=True)
    Share_Date    = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.UserName.username
