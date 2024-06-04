from rest_framework import serializers
from .models import User, Passport, Sitter, Pet, Owner, Admin


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'patronym',
            'tg_name',
            'is_sitter',
            'city',
            'address',
        )


class SitterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sitter
        fields = (
            'birth_date',
            'social',
            'about',
            'animals',
            'avatar',
        )


class PassportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passport
        fields = (
            'pass_num',
            'given_dt',
            'given_code',
            'given_nm',
            'first_nm',
            'second_nm',
            'sur_nm',
            'birth_dt',
            'addr_nm',
            'pic_img',
        )


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = (
            'species',
            'breed',
            'name',
            'gender',
            'sterilized',
            'birth_year',
            'weigth',
            'immunized',
            'vet_ppt',
            'emergency_contact',
            'disease',
            'features'
        )
