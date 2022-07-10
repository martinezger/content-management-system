from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=180)
    content = models.TextField()
    image = models.ImageField(upload_to="articles", null=True, blank=True)
    is_headline= models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()


class Portal(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
