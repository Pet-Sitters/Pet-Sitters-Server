from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from app.views import SitterSerializerAPI

router = SimpleRouter()
router.register(r'sitter_crud', SitterSerializerAPI, basename='sitter')


urlpatterns = [
    path('', include(router.urls)),
]
