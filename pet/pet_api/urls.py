from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PetSerializerAPI

router = SimpleRouter()
router.register(r'pet_crud', PetSerializerAPI, basename='pet')


urlpatterns = [
    path('', include(router.urls)),
]
