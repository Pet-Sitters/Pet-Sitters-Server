from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated
from .serializers import ShortFormSerializer
from app.models import ShortForm


class ShortFormSerializerAPI(viewsets.ModelViewSet):
    queryset = ShortForm.objects.all()
    serializer_class = ShortFormSerializer