from rest_framework import serializers
from .models import Author, Book
from datetime import date


# Serializer for the Book model.
# - Maps model fields to JSON for API representation.
# - Includes validation to ensure publication_year is not in the future.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, data):
        current_year = date.today().year
        if data['publication_year'] > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")


# Serializer for the Author model.
# - Serializes Author fields.
# - Demonstrates nested serialization by including BookSerializer,
#   so an Author can be represented together with their related books.
#   (e.g., returning an author's details along with all books they wrote).

class AuthorSerializer(serializers.ModelSerializer):
    name = BookSerializer()

    class Meta:
        model = Author
        fields = '__all__'