from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import KeepSerializerAPI, ActiveKeepSerializerAPI, NewKeepSerializerAPI

router = SimpleRouter()
router.register(r'keep_crud', KeepSerializerAPI, basename='all_keeps')
router.register(r'active_keep_crud', ActiveKeepSerializerAPI, basename='active_keeps')
router.register(r'new_keep_crud', NewKeepSerializerAPI, basename='new_keeps')
# router.register(r'done_keep_crud', DoneKeepSerializerAPI, basename='done_keeps')


urlpatterns = [
    path('', include(router.urls)),
]
