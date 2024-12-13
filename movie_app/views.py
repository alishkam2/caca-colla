# movie_app/views.py

from rest_framework import viewsets
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    @action(detail=False, methods=["get"])
    def directors_with_movies(self, request):
        directors = Director.objects.annotate(movies_count=models.Count("movies"))
        serializer = self.get_serializer(directors, many=True)
        return Response(serializer.data)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=False, methods=["get"])
    def movies_with_reviews(self, request):
        movies = Movie.objects.all()
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
