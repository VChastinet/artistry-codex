from django.urls import include, path
from rest_framework import routers

from artists.viewsets import ArtistsViewSet, TagsViewSet, StatesViewSet

router = routers.DefaultRouter()
router.register(r'tags', TagsViewSet)
router.register(r'states', StatesViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('artists/', ArtistsViewSet.as_view({'get': 'list'})),
  path('artist/<int:pk>/', ArtistsViewSet.as_view({'get': 'retrieve'})),
  path('artists-by-tag/<int:tag_id>', ArtistsViewSet.as_view({'get': 'artist_by_tag'})),
  path('artists-by-state/<str:uf>', ArtistsViewSet.as_view({'get': 'artist_by_state'})),
]