from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name


class Member(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    weight = models.CharField(max_length=100, null=True, blank=True)
    relation = models.CharField(max_length=100, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

class Test(models.Model):
    fullname = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE, null=True, blank=True)
    testname = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    fromdate = models.DateField(null=True, blank=True)
    todate = models.DateField(null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

class Pressure(models.Model):
    fullname = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE, null=True, blank=True)
    sysmmhg = models.CharField(max_length=100, null=True, blank=True)
    diammhg = models.CharField(max_length=100, null=True, blank=True)
    pluses = models.CharField(max_length=100, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

class Sugar(models.Model):
    fullname = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE, null=True, blank=True)
    typesofbloodsugar = models.CharField(max_length=100, null=True, blank=True)
    bloodsugarmgdl = models.CharField(max_length=100, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

class Temprature(models.Model):
    fullname = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE, null=True, blank=True)
    bodytemprature = models.CharField(max_length=100, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)
