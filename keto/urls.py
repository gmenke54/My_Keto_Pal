from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name='profile_list'),
    path('profiles/<int:pk>', views.ProfileDetail.as_view(),
         name='profile_detail'),
    path('days/', views.DayList.as_view(), name='day_list'),
    path('days/<int:pk>', views.DayDetail.as_view(), name='day_detail'),
    path('foods/', views.FoodList.as_view(), name='food_list'),
    path('foods/<int:pk>', views.FoodDetail.as_view(), name='food_detail'),
    path('recipes/', views.RecipeList.as_view(), name='recipe_list'),
    path('recipes/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
]
