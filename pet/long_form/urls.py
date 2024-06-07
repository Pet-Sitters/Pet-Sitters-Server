from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import LongFormSerializerAPI

router = SimpleRouter()
router.register(r'long_form_crud', LongFormSerializerAPI, basename='long_form')


urlpatterns = [
    path('', include(router.urls)),
]
