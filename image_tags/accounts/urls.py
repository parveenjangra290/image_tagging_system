from django.urls import path, include
from rest_framework import routers
from accounts.api import api

router = routers.SimpleRouter()

router.register('users', api.UserAPIViewSet, basename='account')

urlpatterns = [
    path('', include(router.urls)),
]
