from rest_framework import serializers
from rest_framework.serializers import ImageField
from .models import User, Passport, Sitter, Pet, Owner, Admin, HomeImages
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'patronym',
            'email',
            'tg_name',
            'city',
            'address',
        )


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


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = '__all__'
