from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='songs')
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.title} -> {self.author}"
