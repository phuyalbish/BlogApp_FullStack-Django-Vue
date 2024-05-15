from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    description = models.CharField(max_length=200, null=True)
    modified_by = models.CharField(max_length=50, null=True)