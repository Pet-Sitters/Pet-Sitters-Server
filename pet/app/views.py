from rest_framework import viewsets, response
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer
from .models import CustomUser


class UserSerializerAPI(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
