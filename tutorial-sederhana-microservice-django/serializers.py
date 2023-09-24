from rest_framework import serializers
from .models import MovieData, Review

class MovieSerializer(serializers.ModelSerializer):
	image = serializers.ImageField(max_length=None, use_url=True)
	class Meta:
		model = Moviedata
		fields = ['id', 'name', 'duration', 'rating', 'typ', 'image']
	
class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = ['id', 'movie', 'user', 'comment', 'rating']