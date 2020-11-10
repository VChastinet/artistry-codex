from django.urls import include, path, re_path
from rest_framework import routers

from artists.viewsets import ArtistsViewSet, TagsViewSet, StatesViewSet

router = routers.DefaultRouter()
router.register(r'tags', TagsViewSet)
router.register(r'states', StatesViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('artists/', ArtistsViewSet.as_view({'get': 'list'})),
  path('artist/<int:id>/', ArtistsViewSet.as_view({'get': 'retrieve'})),
]