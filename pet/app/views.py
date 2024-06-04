from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, SitterSerializer, PetSerializer, PassportSerializer
from .models import User, Sitter, Pet, Passport


class UserSerializerAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )


class SitterSerializerAPI(viewsets.ModelViewSet):
    queryset = Sitter.objects.all()
    serializer_class = SitterSerializer


class PassportSerializerAPI(viewsets.ModelViewSet):
    queryset = Passport
    serializer_class = PassportSerializer


class PetSerializerAPI(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
