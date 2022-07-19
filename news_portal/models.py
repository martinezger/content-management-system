from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Publisher(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    avatar = models.ImageField(upload_to="avatars", null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"


class Article(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=180)
    content = RichTextField()
    image = models.ImageField(upload_to="articles", null=True, blank=True)
    author = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    is_headline= models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()


class Portal(models.Model):
    name = models.CharField(max_length=20)
    social_network_one = models.URLField(null=True)
    social_network_two = models.URLField(null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
