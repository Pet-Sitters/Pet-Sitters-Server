from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer
from .models import User


class UserSerializerAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )

