from rest_framework import serializers
from .models import User, Profile, Day, Meal, Food

# BROKEN:
# class ProfileSerializer(serializers.HyperlinkedModelSerializer):
#     days = serializers.HyperlinkedRelatedField(
#         view_name='day_detail',
#         many=True,
#         read_only=True
#     )

#     profile_url = serializers.ModelSerializer.serializer_url_field(
#         view_name='profile_detail'
#     )

#     user = serializers.HyperlinkedRelatedField(
#         view_name='user_detail',
#         read_only=True
#     )

#     user_id = serializers.PrimaryKeyRelatedField(
#         queryset=User.objects.all(),
#         source='user'
#     )

#     class Meta:
#         model = Profile
#         fields = ('id', 'profile_url', 'user', 'user_id', 'cur_weight',
#                   'goal_weight', 'img', 'keto_weeks', 'days', )


# class DaySerializer(serializers.HyperlinkedModelSerializer):
#     meals = serializers.HyperlinkedRelatedField(
#         view_name='meal_detail',
#         many=True,
#         read_only=True
#     )

#     day_url = serializers.ModelSerializer.serializer_url_field(
#         view_name='day_detail'
#     )

#     user = serializers.HyperlinkedRelatedField(
#         view_name='user_detail',
#         read_only=True
#     )

#     user_id = serializers.PrimaryKeyRelatedField(
#         queryset=User.objects.all(),
#         source='user'
#     )

#     class Meta:
#         model = Day
#         fields = ('id', 'day_url', 'user', 'user_id', 'date', 'meals', )


class DaySerializer(serializers.ModelSerializer):
    meals = serializers.PrimaryKeyRelatedField(
        queryset=Meal.objects.all(),
        many=True,
    )

    day_url = serializers.ModelSerializer.serializer_url_field(
        view_name='day_detail'
    )

    # user = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     read_only=True
    # )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )

    class Meta:
        model = Day
        fields = ('id', 'day_url', 'user_id', 'date', 'meals', )


class ProfileSerializer(serializers.ModelSerializer):
    # days = serializers.PrimaryKeyRelatedField(
    #     queryset=Day.objects.all(),
    #     many=True,
    # )
    days = DaySerializer(many=True, read_only=True)

    profile_url = serializers.ModelSerializer.serializer_url_field(
        view_name='profile_detail'
    )

    # user = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     read_only=True
    # )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )

    class Meta:
        model = Profile
        fields = ('days', 'user', 'profile_url', 'user_id', 'cur_weight',
                  'goal_weight', 'img', 'keto_weeks',)

# Working:


class FoodSerializer(serializers.ModelSerializer):
    meals = serializers.PrimaryKeyRelatedField(
        queryset=Meal.objects.all(),
        many=True,
    )

    food_url = serializers.ModelSerializer.serializer_url_field(
        view_name='food_detail'
    )

    class Meta:
        model = Food
        fields = ('id', 'food_url', 'meals', 'name', 'weight', 'carbs', 'calories', 'fat', 'protein',
                  'sugar', 'fiber', 'saturated', 'trans', 'chol', 'sodium', 'added_sugar', 'chol_dv', 'sodium_dv', )


class MealSerializer(serializers.ModelSerializer):
    food_list = FoodSerializer(
        many=True,
        read_only=True
    )

    meal_url = serializers.ModelSerializer.serializer_url_field(
        view_name='meal_detail'
    )

    day = serializers.HyperlinkedRelatedField(
        view_name='day_detail',
        read_only=True
    )

    day_id = serializers.PrimaryKeyRelatedField(
        queryset=Day.objects.all(),
        source='day'
    )

    class Meta:
        model = Meal
        fields = ('id', 'meal_url', 'food_list', 'day', 'day_id', 'name', )
