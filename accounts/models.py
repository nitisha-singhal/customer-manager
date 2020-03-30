from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.utils import timezone

class user(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    skills = RichTextField()
    country = models.CharField(max_length=50)
    company = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    email = models.EmailField()

class upcoming(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    comm_via = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class running(models.Model):
    title = models.CharField(max_length=100)
    progress = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class pending(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    client = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class deadlines(models.Model):
    client = models.CharField(max_length=50)
    deadline = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.client