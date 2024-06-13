from rest_framework import viewsets, response
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, OwnerSerializer
from .models import CustomUser, Owner


class UserSerializerAPI(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )

class OwnerSerializerAPI(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
