from rest_framework import serializers
from app.models import Owner


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = '__all__'