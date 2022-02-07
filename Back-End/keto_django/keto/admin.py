from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Day, Meal, Food

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Day)
admin.site.register(Meal)
admin.site.register(Food)
