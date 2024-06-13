from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from .views import UserSerializerAPI, OwnerSerializerAPI

router = SimpleRouter()
router.register(r'user_crud', UserSerializerAPI, basename='user')
router.register(r'owner_crud', OwnerSerializerAPI, basename='owner')


urlpatterns = [
    path('', include(router.urls)),
]
