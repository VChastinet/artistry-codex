from . import models

from rest_framework import serializers


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.State
        fields = ['uf', 'id', 'name']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    state = StateSerializer()

    class Meta:
        model = models.Artist
        fields = '__all__'