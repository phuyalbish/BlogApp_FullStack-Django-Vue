from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    description = models.CharField()