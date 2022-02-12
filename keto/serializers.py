from rest_framework import serializers
from .models import User, Profile, Day, Food, Comment, Recipe, Post


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
        fields = ('profile', 'recipe', 'post', 'comments', 'rating', )


class RecipeSerializer(serializers.ModelSerializer):
    comment_list = CommentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Recipe
        fields = ('type', 'profile', 'comment_list', 'days', 'servings', 'name', 'instructions', 'ingredients', 'weight', 'carbs', 'calories',
                  'fat', 'protein', 'sugar', 'fiber', 'saturated', 'trans', 'chol', 'sodium', 'added_sugar', 'chol_dv', 'sodium_dv', )


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Post
        fields = ('id', 'type', 'comments', 'profile', 'text', 'img', 'link',)


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
        fields = ('id', 'day_url', 'user_id', 'date',
                  'food_list', 'recipes_eaten')


class ProfileSerializer(serializers.ModelSerializer):
    days = DaySerializer(
        many=True,
        read_only=True
    )

    my_recipes = RecipeSerializer(
        many=True,
        read_only=True
    )

    my_posts = PostSerializer(
        many=True,
        read_only=True
    )

    my_comments = CommentSerializer(
        many=True,
        read_only=True
    )

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
                  'goal_weight', 'img', 'keto_weeks', 'name', 'age', 'activ', 'my_recipes', 'my_posts', 'my_comments', 'daily_carb', 'daily_fat', 'daily_sugar')
