# from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProfileSerializer, DaySerializer, FoodSerializer
from .models import Profile, Day, Food


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class DayList(generics.ListCreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class DayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


# class GetDayByUser(APIView):
#     queryset = Day.objects.all()

#     def get(request):
#         print(request.data)
#         return Response


# class MealList(generics.ListCreateAPIView):
#     queryset = Meal.objects.all()
#     serializer_class = MealSerializer


# class MealDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Meal.objects.all()
#     serializer_class = MealSerializer


class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
