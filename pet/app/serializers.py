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

