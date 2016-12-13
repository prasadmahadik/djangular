from rest_framework import serializers

from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =('author','description','title')
