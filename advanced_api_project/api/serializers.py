from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_book_): handel books instances in database

    Raises:
        serializers.ValidationError: if publication year is in the future raise error

    Returns:
        int: publication year
    """
    class Meta:
        model = Book
        fields = '__all__'
        def validate(self, attrs):
            if attrs['publication_year'] > 2024:
                raise serializers.ValidationError("Publication year cannot be in the future")
            return attrs
        
class AuthorSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (Authors): handel authors instances in database
    """
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']