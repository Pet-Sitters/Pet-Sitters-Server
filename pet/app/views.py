from rest_framework import viewsets, response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, SitterSerializer, PetSerializer, LongFormSerializer, ShortFormSerializer
from .models import User, Sitter, Pet, Passport, Keep, ShortForm


class UserSerializerAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )


class SitterSerializerAPI(viewsets.ModelViewSet):
    queryset = Sitter.objects.all()
    serializer_class = SitterSerializer
    permission_classes = [IsAuthenticated]


class PetSerializerAPI(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user.id)
            return response.Response(request.data)

class LongFormSerializerAPI(viewsets.ModelViewSet):
    queryset = Keep.objects.filter(is_active=True)
    serializer_class = LongFormSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = LongFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user.id)
            return response.Response(request.data)


class ShortFormSerializerAPI(viewsets.ModelViewSet):
    queryset = ShortForm.objects.all()
    serializer_class = ShortFormSerializer
