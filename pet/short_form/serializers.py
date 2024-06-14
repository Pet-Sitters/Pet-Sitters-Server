from rest_framework import serializers
from app.models import ShortForm, Owner, Keep, CustomUser
from app.serializers import UserSerializer


class ShortFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortForm
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        current_user = validated_data.pop('user')
        owner, created = Owner.objects.get_or_create(user=current_user)
        new_keep = Keep.objects.create(owner=owner, status='new')
        form_data = ShortForm.objects.create(user=current_user, **validated_data)
        return owner, new_keep, form_data