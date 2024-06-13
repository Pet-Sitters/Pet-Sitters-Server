from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ActiveKeepSerializerAPI

router = SimpleRouter()
router.register(r'active_keep_crud', ActiveKeepSerializerAPI, basename='active_keep')


urlpatterns = [
    path('', include(router.urls)),
]
