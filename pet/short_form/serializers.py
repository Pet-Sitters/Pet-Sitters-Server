from rest_framework import serializers
from app.models import ShortForm


class ShortFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortForm
        fields = '__all__'