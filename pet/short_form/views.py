from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated
from .serializers import ShortFormSerializer
from app.models import ShortForm


class ShortFormSerializerAPI(viewsets.ModelViewSet):
    queryset = ShortForm.objects.all()
    serializer_class = ShortFormSerializer

    def create(self, request, *args, **kwargs):
        serializer = ShortFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return response.Response(request.data)
