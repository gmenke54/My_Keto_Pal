from rest_framework import serializers
from .models import User, Profile, Day, Food, Comment, Recipe


class FoodSerializer(serializers.ModelSerializer):
    days = serializers.PrimaryKeyRelatedField(
        queryset=Day.objects.all(),
        many=True,
    )

    food_url = serializers.ModelSerializer.serializer_url_field(
        view_name='food_detail'
    )

    class Meta:
        model = Food
        fields = ('id', 'food_url', 'days', 'name', 'weight', 'carbs', 'calories', 'fat', 'protein',
                  'sugar', 'fiber', 'saturated', 'trans', 'chol', 'sodium', 'added_sugar', 'chol_dv', 'sodium_dv', )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'recipe', 'comments', 'rating', )


class RecipeSerializer(serializers.ModelSerializer):
    comment_list = CommentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Recipe
        fields = ('user', 'comment_list', 'days', 'servings', 'name', 'instructions', 'ingredients', 'weight', 'carbs', 'calories',
                  'fat', 'protein', 'sugar', 'fiber', 'saturated', 'trans', 'chol', 'sodium', 'added_sugar', 'chol_dv', 'sodium_dv', )


class DaySerializer(serializers.ModelSerializer):
    food_list = FoodSerializer(
        many=True,
        read_only=True
    )

    recipes_eaten = RecipeSerializer(
        many=True,
        read_only=True
    )

    day_url = serializers.ModelSerializer.serializer_url_field(
        view_name='day_detail'
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )

    class Meta:
        model = Day
        fields = ('id', 'day_url', 'user_id', 'date', 'food_list', )


class ProfileSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True, read_only=True)

    profile_url = serializers.ModelSerializer.serializer_url_field(
        view_name='profile_detail'
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )

    class Meta:
        model = Profile
        fields = ('days', 'user', 'profile_url', 'user_id', 'cur_weight',
                  'goal_weight', 'img', 'keto_weeks', 'name', 'age', 'activ')
