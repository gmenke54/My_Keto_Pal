from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        # from stackoverflow: https://stackoverflow.com/questions/26188997/django-model-onetoonefield-without-creating-additional-id-database-column
        # to_field='id',
        # related_name='profile',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    cur_weight = models.FloatField(null=True)
    goal_weight = models.FloatField(null=True)
    img = models.TextField(null=True)
    keto_weeks = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user.username)


class Day(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='days')
    import datetime
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return str(f'{self.user} - {self.date.month}/{self.date.day}/{self.date.year}')


class Meal(models.Model):
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name='meals'
    )
    name = models.CharField(max_length=25, default="Breakfast")

    def __str__(self):
        # return self.name
        return str(f'{self.day} - {self.name}')


class Food(models.Model):
    meals = models.ManyToManyField(
        Meal, related_name="food_list", blank=True
    )
    name = models.CharField(max_length=100)
    weight = models.FloatField(default=0.0)
    carbs = models.FloatField(default=0.0)
    calories = models.FloatField(default=0.0)
    fat = models.FloatField(default=0.0)
    protein = models.FloatField(default=0.0)
    sugar = models.FloatField(default=0.0)
    fiber = models.FloatField(default=0.0)
    saturated = models.FloatField(default=0.0)
    trans = models.FloatField(default=0.0)
    chol = models.FloatField(default=0.0)
    sodium = models.FloatField(default=0.0)
    added_sugar = models.FloatField(default=0.0)
    chol_dv = models.FloatField(default=0.0)
    sodium_dv = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
