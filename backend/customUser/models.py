from django.db import models
from .manager import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AccessToken(models.Model):
    userid = models.IntegerField()
    jti = models.CharField(max_length=100, unique=True, null=False)

class  Users(AbstractBaseUser, PermissionsMixin):
    username: None
    email = models.CharField(max_length=50, null=False, unique=True)
    name = models.CharField(max_length=50, null=True)
    bio = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, default="Male")
    img_src = models.CharField(max_length=100, null=True)
    modified_by = models.CharField(max_length=50, null=True)
    total_follower = models.IntegerField(default=0)
    total_post = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELD = []

    def __str__(self):
        return self.name
    
# class Follow(models.Model):
#     follower_id = models.ForeignKey(Users,null=True, on_delete=models.SET_NULL)
#     followedto_id = models.ForeignKey(Users,null=True, on_delete=models.SET_NULL)
#     follower_name = models.CharField(max_length=50, null=True)






