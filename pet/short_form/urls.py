from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from .views import ShortFormSerializerAPI

router = SimpleRouter()
router.register(r'short_form_crud', ShortFormSerializerAPI, basename='short_form')


urlpatterns = [
    path('', include(router.urls)),
]
