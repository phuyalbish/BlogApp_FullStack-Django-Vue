from django.db import models
from customUser.models import Users
from article.models import Articles

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    description = models.CharField(max_length=200, null=True)
    modified_by = models.CharField(max_length=50, null=True)

class Interest(models.Model):
    name = models.CharField(max_length=50, null=True)
    category_id = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)

class ArticleCategory(models.Model):
    name = models.CharField(max_length=50, null=True)
    category_id = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    article_id = models.ForeignKey(Articles, null=True, on_delete=models.SET_NULL)

