from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    cur_weight = models.FloatField(null=True)
    goal_weight = models.FloatField(null=True)
    img = models.TextField(null=True)

    def __str__(self):
        return self.user
