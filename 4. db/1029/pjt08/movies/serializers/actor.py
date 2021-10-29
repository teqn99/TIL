from rest_framework import serializers
from ..models import Actor


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('pk', 'name', )


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('pk', 'name', 'movies')