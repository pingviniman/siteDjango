from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=30)