from django.db import models
from datetime import datetime

# Create your models here.
class userSignup(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()


class feedback(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()

class milanagent(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    message=models.TextField()


class blogreply(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    website=models.URLField()
    message=models.TextField()