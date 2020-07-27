from django.db import models


# Create your models here.

class Video_list(models.Model):
    Title = models.CharField(max_length=500)
    Author = models.CharField(max_length=500)
    VideoFile = models.FileField(upload_to='videos-list')

    def __str__(self):
        return self.Title


class Image_list(models.Model):
    name = models.CharField(max_length=500)
    pdf = models.FileField(upload_to='img-list')

    def __str__(self):
        return self.name


class Post_Blog(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=10)
    body = models.TextField()
    File_f = models.FileField(upload_to='post-media/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
