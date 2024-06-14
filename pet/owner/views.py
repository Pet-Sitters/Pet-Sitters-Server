from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .serializers import OwnerSerializer
from app.models import Owner


class OwnerSerializerAPI(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer