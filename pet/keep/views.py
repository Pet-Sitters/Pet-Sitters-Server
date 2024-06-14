from rest_framework import viewsets, response
from .serializers import KeepSerializer, ActiveKeepSerializer
from app.models import Keep


class KeepSerializerAPI(viewsets.ModelViewSet):
    queryset = Keep.objects.all()
    serializer_class = KeepSerializer

    # def get_queryset(self):
    #     qr = Keep.objects.all()
    #     qr_filter = Keep.objects.filter(status='active')
    #     if qr_filter:
    #         return qr_filter
    #     return qr

    # def create(self, request, *args, **kwargs):
    #     serializer = ActiveKeepSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return response.Response(request.data)

class ActiveKeepSerializerAPI(viewsets.ModelViewSet):
    serializer_class = ActiveKeepSerializer
    queryset = Keep.objects.filter(status='active')


class NewKeepSerializerAPI(viewsets.ModelViewSet):
    serializer_class = KeepSerializer
    queryset = Keep.objects.filter(status='new')


# class ProcessKeepSerializerAPI(viewsets.ModelViewSet):
#     serializer_class = KeepSerializer
#     queryset = Keep.objects.filter(status='in_process')
#     http_method_names = ['get', 'patch']
#
#
# class DoneKeepSerializerAPI(viewsets.ModelViewSet):
#     serializer_class = KeepSerializer
#     queryset = Keep.objects.filter(status='done')
#     http_method_names = ['get']
