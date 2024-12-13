# movie_app/serializers.py

from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(source="movies.count", read_only=True)

    class Meta:
        model = Director
        fields = ["id", "name", "movies_count"]


class MovieSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "director",
            "reviews",
            "rating",
        ]

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum([review.stars for review in reviews]) / len(reviews)
        return None


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "text", "movie", "stars"]
