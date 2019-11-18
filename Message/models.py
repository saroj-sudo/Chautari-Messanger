from django.db import models

class Message(models.Model):
    sender=models.IntegerField()
    receiver=models.IntegerField()
    body=models.CharField(max_length=100)


    