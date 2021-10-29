from rest_framework import serializers
from ..models import Movie, Review


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('pk', 'title', )


class ReviewSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'title')
    
    movies = MovieSerializer(read_only=True)  # POST 입력 시 입력 필요 X => read_only이므로

    def create(self, validated_data):
        review = Review.objects.create(**validated_data)
        return review

    def update(self, review, validated_data):
        for attr, value in validated_data.items():
            setattr(review, attr, value)
            review.save()
        return review

    class Meta:
        model = Review
        fields = '__all__'