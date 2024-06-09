from rest_framework import serializers
from app.models import Pet, Owner, Keep
from pet_api.serializers import PetSerializer
from drf_writable_nested import WritableNestedModelSerializer


class LongFormSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    pet = PetSerializer()

    class Meta:
        model = Keep
        fields = '__all__'

    def create(self, validated_data):
        current_user = validated_data.pop('user')
        owner, created = Owner.objects.get_or_create(user=current_user)
        pet_info = validated_data.pop('pet')
        new_pet = Pet.objects.create(owner=owner, **pet_info)
        new_keep = Keep.objects.create(owner=owner, pet=new_pet, is_active=True, **validated_data)
        return owner, new_pet, new_keep, user