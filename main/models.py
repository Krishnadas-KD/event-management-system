from pyexpat import model
from django.db import models

# Create your models here.


class admininfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)

class teacherinfo(models.Model):
    tid = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    mangingfevent=models.CharField(default="Not selected",max_length=50)
    password = models.CharField(max_length=20)


class studentinfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    stclass = models.CharField(max_length=20)
    Admissionno = models.CharField(max_length=20)

class eventgoing(models.Model):
    tempid=models.CharField(max_length=20)
    event=models.CharField(max_length=20)
class resultpublic(models.Model):
    tempid=models.CharField(max_length=20)
    result=models.CharField(max_length=20)
class event(models.Model):
    aors=models.CharField(max_length=20)
    event=models.CharField(max_length=20)

class studentevent(models.Model):
    event=models.CharField(max_length=50)
    chestno=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    grade=models.CharField(default="Not graded",max_length=20)
    