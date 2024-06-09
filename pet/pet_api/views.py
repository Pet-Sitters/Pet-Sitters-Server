from rest_framework import viewsets, response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PetSerializer
from app.models import Pet, Owner


class PetSerializerAPI(viewsets.ModelViewSet):
    # queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user.id)
            return response.Response(request.data)

    def get_queryset(self):
        user = self.request.user.id
        try:
            owner = Owner.objects.get(user=user)
            pet_list = Pet.objects.filter(owner=owner)
            return pet_list
        except:
            return response.Response({'error': 'This user is not an owner yet!'})
