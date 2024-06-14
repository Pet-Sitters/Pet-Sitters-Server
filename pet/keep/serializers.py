from rest_framework import serializers
from app.models import Owner, Keep
from pet_api.serializers import PetSerializer
from app.serializers import OwnerSerializer
from drf_writable_nested import WritableNestedModelSerializer


class KeepSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):

    class Meta:
        model = Keep
        fields = '__all__'


class ActiveKeepSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    owner = OwnerSerializer()
    pet = PetSerializer()

    class Meta:
        model = Keep
        fields = '__all__'
        read_only_fields = ['owner', 'pet', ]

