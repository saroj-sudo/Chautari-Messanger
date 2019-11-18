from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    img_url=models.URLField(blank=True)

class Comment(models.Model):
    body=models.TextField()
    commentor=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    post = models.ForeignKey(Post,on_delete=models.CASCADE)