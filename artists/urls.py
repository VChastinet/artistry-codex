from django.conf.urls import url
from django.urls import include, path, re_path
from rest_framework import routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from artists.viewsets import ArtistsViewSet, TagsViewSet, StatesViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="Artists API",
        default_version='v1',
        description="Api to list artists",
        contact=openapi.Contact(url="https://chastinet.dev"),
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register(r'tags', TagsViewSet)
router.register(r'states', StatesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('artists/', ArtistsViewSet.as_view({'get': 'list'})),
    path('artist/<int:pk>/', ArtistsViewSet.as_view({'get': 'retrieve'})),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
