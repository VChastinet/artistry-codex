from django.db.models import Count
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from artists.serializers import ArtistSerializer, StateSerializer, TagSerializer
from . import models


class ArtistsViewSet(viewsets.ModelViewSet):
  queryset = models.Artist.objects.all()
  serializer_class = ArtistSerializer

  def list(self, request, *args, **kwargs):
    tag_params = request.GET.get('tags')
    name_params = request.GET.get('name')
    uf_params = request.GET.get('uf')
    
    if tag_params:
      return self.artist_by_tag(request, tag_params)
    elif name_params:
      return self.artist_by_name(request, name_params)
    elif uf_params:
      return self.artist_by_state(request, uf_params)
    else:
      return super().list(request, *args, **kwargs)
  
  def artist_by_tag(self, request, tag_params):
    tags = tag_params.split(',')
    queryset = self.get_queryset().filter(tags__in=tags).annotate(num_tags=Count('tags')).filter(num_tags__gte=len(tags))
    page = self.paginate_queryset(queryset)
    serialize = self.get_serializer(page, many=True)

    return self.get_paginated_response(serialize.data)

  def artist_by_state(self, request, uf_params):
    queryset = self.get_queryset().filter(state__uf=uf_params.upper())
    page = self.paginate_queryset(queryset)
    serialize = self.get_serializer(page, many=True)

    return self.get_paginated_response(serialize.data)

    
  def artist_by_name(self, request, name_params):
    queryset = self.get_queryset().filter(name__icontains=name_params)
    page = self.paginate_queryset(queryset)
    serialize = self.get_serializer(page, many=True)

    return self.get_paginated_response(serialize.data)


class TagsViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = models.Tag.objects.all()
  serializer_class = TagSerializer


class StatesViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = models.State.objects.all()
  serializer_class = StateSerializer