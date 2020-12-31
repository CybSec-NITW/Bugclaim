from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group

User = settings.AUTH_USER_MODEL


class Researcher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, max_length=100, default="")
    country = models.CharField(max_length=20, blank=True, default="")
    facebook_url = models.URLField(blank=True, default="")
    twitter_handler = models.CharField(max_length=40, blank=True, default="")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username

    class Meta:
        db_table = 'researcher'
