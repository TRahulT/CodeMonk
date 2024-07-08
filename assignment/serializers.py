from rest_framework import serializers
from .models import Paragraph,Word,CustomUser

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paragraph
        fields=['id', 'text']

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Word
        fields=['word','paragraph']

class CustomUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserLoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    def validate(self, data):
        name = data.get('name')
        email = data.get('email')

        # Check if a user exists with this name and email combination
        if not CustomUser.objects.filter(name=name, email=email).exists():
            raise serializers.ValidationError("User with this name and email does not exist.")
        return data