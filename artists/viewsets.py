from rest_framework import viewsets
from rest_framework.response import Response

from artists.serializers import ArtistSerializer, StateSerializer, TagSerializer
from . import models


class ArtistsViewSet(viewsets.ModelViewSet):
  
  queryset = models.Artist.objects.all()
  serializer_class = ArtistSerializer

  def artist_by_tag(self, request, tag_id):

    queryset = self.queryset.filter(tags=tag_id)
    page = self.paginate_queryset(queryset)
    serialize = self.get_serializer(page, many=True)

    return self.get_paginated_response(serialize.data)

  def artist_by_state(self, request, uf):

    queryset = self.queryset.filter(state__uf=uf.upper())
    page = self.paginate_queryset(queryset)
    serialize = self.get_serializer(page, many=True)

    return self.get_paginated_response(serialize.data)


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = models.Tag.objects.all()
  serializer_class = TagSerializer


class StatesViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = models.State.objects.all()
  serializer_class = StateSerializer