from rest_framework import serializers
from rest_framework.serializers import ImageField
from .models import User, Passport, Sitter, Pet, Owner, Admin, HomeImages, Keep
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'patronym',
            'email',
            'tg_nick',
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


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = '__all__'


class LongFormSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    pet = PetSerializer()

    class Meta:
        model = Keep
        exclude = ['is_active', 'sitter', 'owner']

    def create(self, validated_data):
        current_user = validated_data.pop('user')
        owner, created = Owner.objects.get_or_create(user=current_user)
        pet_info = validated_data.pop('pet')
        new_pet, created = Pet.objects.get_or_create(owner=owner)
        new_keep = Keep.objects.create(owner=owner, is_active=True, **validated_data)
        return owner, new_pet, new_keep


class ShortFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'tg_nick', 'phone_num', ]

    def create(self, validated_data):
        current_user = validated_data.pop('user')
        filled_user = User(id=current_user, **validated_data)
        new_owner, created = Owner.objects.get_or_create(user=current_user)
        new_keep = Keep.objects.create(owner=new_owner, is_active=False)
        return new_keep, new_owner


class ActiveOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keep
        fields = '__all__'


class InactiveOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keep
        fields = '__all__'
