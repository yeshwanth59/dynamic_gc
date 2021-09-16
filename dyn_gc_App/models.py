from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField()
    dob = models.DateField()


class Master(models.Model):
    thumbnails = models.ImageField(upload_to='upload/thumbnails', blank=True)


class Plot(models.Model):
    plot_num = models.IntegerField(blank=False)
    plot_size = models.CharField(max_length=20)
    status = models.CharField(max_length=20)