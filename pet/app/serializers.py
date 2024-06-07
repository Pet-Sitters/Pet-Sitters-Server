from rest_framework import serializers
from .models import CustomUser, Owner


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'patronym',
            'email',
            'tg_nick',
            'city',
            'address',
        )


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'
