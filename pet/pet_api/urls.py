from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from app.views import PetSerializerAPI

router = SimpleRouter()
router.register(r'pet_crud', PetSerializerAPI, basename='pet')


urlpatterns = [
    path('', include(router.urls)),
]
