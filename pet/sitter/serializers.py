from rest_framework import serializers
from app.models import HomeImages, Passport, Sitter
from app.serializers import UserSerializer
from drf_writable_nested import WritableNestedModelSerializer


class HomeImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeImages
        fields = ['image']


class PassportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passport
        exclude = ('sitter', )


class SitterSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = UserSerializer()
    images = HomeImagesSerializer(many=True)
    passport = PassportSerializer()

    class Meta:
        model = Sitter
        exclude = ['rating', 'game', 'activated']