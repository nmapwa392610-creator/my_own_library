from rest_framework import serializers
from .models import Book,Author,BookReading


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='name',read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookReadingSerializer(serializers.Serializer):
    class Meta:
        model = BookReading
        fields = '__all__'