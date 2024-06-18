from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import SitterSerializer
from app.models import Sitter


class SitterSerializerAPI(viewsets.ModelViewSet):
    queryset = Sitter.objects.all()
    serializer_class = SitterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)