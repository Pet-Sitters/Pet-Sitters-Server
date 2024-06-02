from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from .views import UserSerializerAPI


router = SimpleRouter()
router.register(r'user_crud', UserSerializerAPI, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]
