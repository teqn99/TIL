from rest_framework import serializers
from ..models import Movie, Actor, Review


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title', )


class MovieSerializer(serializers.ModelSerializer):

    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('pk', 'name', )

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('pk', 'title')

    reviews = ReviewSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    actor_pks = serializers.ListField(write_only=True)

    def create(self, validated_data):
        actor_pks = validated_data.pop('actor_pks')
        movie = Movie.objects.create(**validated_data)
        for actor_pk in actor_pks:
            movie.actors.add(actor_pk)
        return movie

    class Meta:
        model = Movie
        fields = '__all__'