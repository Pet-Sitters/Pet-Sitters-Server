from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated
from .serializers import SitterSerializer
from app.models import Sitter


class SitterSerializerAPI(viewsets.ModelViewSet):
    queryset = Sitter.objects.all()
    serializer_class = SitterSerializer
    permission_classes = [IsAuthenticated]