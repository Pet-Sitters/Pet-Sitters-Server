from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated
from .serializers import LongFormSerializer
from app.models import Keep


class LongFormSerializerAPI(viewsets.ModelViewSet):
    queryset = Keep.objects.filter(is_active=True)
    serializer_class = LongFormSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = LongFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user.id)
            return response.Response(request.data)