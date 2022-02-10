from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Day, Food, Recipe, Comment

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Day)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Food)
