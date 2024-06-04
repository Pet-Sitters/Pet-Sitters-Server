from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from .views import UserSerializerAPI, SitterSerializerAPI, PassportSerializerAPI, PetSerializerAPI


router = SimpleRouter()
router.register(r'user_crud', UserSerializerAPI, basename='user')
router.register(r'sitter_crud', SitterSerializerAPI, basename='sitter')
router.register(r'passport_crud', PassportSerializerAPI, basename='passport')
router.register(r'pet_crud', PetSerializerAPI, basename='pet')


urlpatterns = [
    path('', include(router.urls)),
]
