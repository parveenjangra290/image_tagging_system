"""
    Image & Tag API URLs.
"""

from django.urls import path, include
from rest_framework import routers
from image_tag_api.api import api

router = routers.SimpleRouter()

router.register('', api.TagAPIViewSet, basename='tag-create')
router.register('', api.ImageAPIViewSet, basename='image-create')

urlpatterns = [
    path('', include(router.urls)),
]
