from rest_framework import viewsets, response
from .serializers import ActiveKeepSerializer
from app.models import ActiveKeep


class ActiveKeepSerializerAPI(viewsets.ModelViewSet):
    queryset = ActiveKeep.objects.filter()
    serializer_class = ActiveKeepSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = ActiveKeepSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user.id)
    #         return response.Response(request.data)