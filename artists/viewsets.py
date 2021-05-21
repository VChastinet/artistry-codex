from django.db.models import Count
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from artists.serializers import ArtistSerializer, StateSerializer, TagSerializer
from . import models


class ArtistsViewSet(viewsets.ModelViewSet):
  """Returns a list of artists filtered by params.

  @params tags
  @params name
  @params uf
  """

  queryset = models.Artist.objects.all()
  serializer_class = ArtistSerializer

  tags = openapi.Parameter('tags', openapi.IN_QUERY, description="one or more tag id", type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER))
  name = openapi.Parameter('name', openapi.IN_QUERY, description="name (or part of) of the artist", type=openapi.TYPE_STRING)
  uf = openapi.Parameter('uf', openapi.IN_QUERY, description="State's inital", type=openapi.TYPE_STRING)

  @swagger_auto_schema(manual_parameters=[tags, name, uf])
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
    # queryset = self.get_queryset().filter(tags__in=tags).annotate(num_tags=Count('tags')).filter(num_tags__gte=len(tags))
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
