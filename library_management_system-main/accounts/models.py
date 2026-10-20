from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):

    full_name = models.CharField(max_length=150, blank=True, null=True)

    phone = models.CharField(max_length=20, blank=True, null=True)

    profile_image = models.ImageField(upload_to='user_img/', blank=True, null=True)

    def __str__(self):
        return self.username
      