from rest_framework import viewsets, response
from .serializers import NewKeepSerializer
from app.models import NewKeepFrom


class NewKeepSerializerAPI(viewsets.ModelViewSet):
    queryset = NewKeepFrom.objects.all()
    serializer_class = NewKeepSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = ShortFormSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return response.Response(request.data)
