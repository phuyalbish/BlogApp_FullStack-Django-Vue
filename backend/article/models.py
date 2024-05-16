from django.db import models
from customUser.models import Users

class Articles(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    description = models.CharField(max_length=200, null=False)
    further_readings = models.CharField(max_length=200)
    authorid = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    authorname = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)
    is_hidden = models.BooleanField(default=False)
    modifiedBy = models.CharField(max_length=50, null=True)
    totalLikes = models.IntegerField(default=0)
    totalComments = models.IntegerField(default=0)
    
