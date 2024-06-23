from rest_framework import serializers
from app.models import HomeImages, Passport, Sitter
from app.serializers import UserSerializer
from drf_writable_nested import WritableNestedModelSerializer


# class HomeImagesSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = HomeImages
#         fields = ['image']


class PassportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passport
        exclude = ('sitter', )


class SitterSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    # user = UserSerializer()
    passport = PassportSerializer()

    class Meta:
        model = Sitter
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
            "patronym",
            "tg_nick",
            "tg_id",
            "phone_num",
            "city",
            "address",
            "birth_date",
            "social",
            "about",
            "home",
            "animals",
            "rating",
            "game",
            "activated",
            "passport"
        ]

        def create(self, validated_data):
            print(validated_data)
            cur_user = validated_data.pop('user')
            pprt_data = validated_data.pop('passport')

            new_sitter = Sitter.objects.create(user=cur_user, **validated_data)
            sitter_passport = Passport.objects.create(sitter=new_sitter, **pprt_data)

            return new_sitter, sitter_passport