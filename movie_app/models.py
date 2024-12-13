# movie_app/models.py

from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()  # продолжительность фильма в минутах
    director = models.ForeignKey(
        Director, related_name="movies", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"Review for {self.movie.title}"
