from rest_framework import serializers
from app.models import Pet, Owner
from app.extensions import AGGRESSION


class PetSerializer(serializers.ModelSerializer):
    # aggression = serializers.MultipleChoiceField(choices=AGGRESSION)

    class Meta:
        model = Pet
        fields = [
            'id',
            'owner',
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
            'diseases',
            'fears',
            'features',
            'outside_lb',
            'scratch',
            'pulls',
            'picks',
            'take',
            'aggression',
            'no_leash',
            'dogs_contact',
            'wash_paws',
            'pee_home',
            'gnaw_home',
            'walk' ,
        ]

    def create(self, validated_data):
        current_user = validated_data.pop('user')
        owner, created = Owner.objects.get_or_create(user=current_user)
        new_pet = Pet.objects.create(owner=owner, **validated_data)
        return new_pet