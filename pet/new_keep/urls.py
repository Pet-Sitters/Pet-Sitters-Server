from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from .views import NewKeepSerializerAPI

router = SimpleRouter()
router.register(r'new_keep_crud', NewKeepSerializerAPI, basename='new_keep')


urlpatterns = [
    path('', include(router.urls)),
]
