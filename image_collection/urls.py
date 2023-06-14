from .views import *
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('image-collection', Image_collectionViewSet, basename='image-collection')

urlpatterns = [
    path('', include(router.urls)),
    path('update-key-points/', update_key_points, name='update-key-points')
]