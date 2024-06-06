from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from app.views import LongFormSerializerAPI

router = SimpleRouter()
router.register(r'long_form_crud', LongFormSerializerAPI, basename='long_form')


urlpatterns = [
    path('', include(router.urls)),
]
