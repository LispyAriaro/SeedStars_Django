from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
