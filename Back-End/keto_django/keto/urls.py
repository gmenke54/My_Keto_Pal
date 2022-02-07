from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name='profile_list'),
    path('profiles/<int:pk>', views.ProfileDetail.as_view(),
         name='profile_detail'),
    path('days/', views.DayList.as_view(), name='day_list'),
    path('days/<int:pk>', views.DayDetail.as_view(), name='day_detail'),
    path('meals/', views.MealList.as_view(), name='meal_list'),
    path('meals/<int:pk>', views.MealDetail.as_view(), name='meal_detail'),
    path('foods/', views.FoodList.as_view(), name='food_list'),
    path('foods/<int:pk>', views.FoodDetail.as_view(), name='food_detail')
]
