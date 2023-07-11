from rest_framework import serializers
from core.models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_date):
        genres_date = validated_date.pop('genres')
        book = Book.objects.create(**validated_date)
        for genre in genres_date:
            gn, _ = Genre.objects.get_or_create(name=genre['name'])
            book.genres.add(gn)
        return book