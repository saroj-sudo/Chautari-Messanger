from django.db import models
from django.contrib.auth.models import User

class Friend(models.Model):
    sender = models.IntegerField()
    receiver = models.IntegerField()

class Friend_request(models.Model):
    sender = models.IntegerField()
    receiver = models.IntegerField()