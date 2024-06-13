from rest_framework import serializers
from app.models import NewKeepFrom, Owner, ActiveKeep, CustomUser
from app.serializers import UserSerializer


class NewKeepSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewKeepFrom
        fields = '__all__'

    # def create(self, validated_data):
    #     current_user = validated_data.pop('user')
    #     owner, created = Owner.objects.get_or_create(user=current_user)
    #     new_keep = Keep.objects.create(owner=owner, is_active=False)
    #     form_data = ShortForm.objects.create(user=current_user, **validated_data)
    #     return owner, new_keep, form_data