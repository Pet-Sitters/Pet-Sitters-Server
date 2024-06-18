from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ShortFormSerializer
from app.models import ShortForm


class ShortFormSerializerAPI(viewsets.ModelViewSet):
    queryset = ShortForm.objects.all()
    serializer_class = ShortFormSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
