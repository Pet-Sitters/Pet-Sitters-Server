from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
# from .views import UserSerializerAPI, SitterSerializerAPI, PassportSerializerAPI, PetSerializerAPI, SitterFormSerializerAPI
from .views import *

router = SimpleRouter()
router.register(r'user_crud', UserSerializerAPI, basename='user')
router.register(r'pet_crud', PetSerializerAPI, basename='pet')
router.register(r'long_form_crud', LongFormSerializerAPI, basename='long_form')
router.register(r'short_form_crud', ShortFormSerializerAPI, basename='short_form')
router.register(r'active_orders_crud', ActiveOrdersSerilizerAPI, basename='active_orders')
router.register(r'inactive_orders_crud', InactiveOrdersSerilizerAPI, basename='inactive_orders')


urlpatterns = [
    path('', include(router.urls)),
]
