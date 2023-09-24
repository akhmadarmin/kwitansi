import requests

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		movie_data = self.get_movie_data(instance.movie_id)
		response_data = {
			'movie': movie_data,
			'review': ReviewSerializer(instance).data
		}
		return Response(response_data)

	def get_movie_data(self, movie_id):
		access_token = self.get_access_token()
		headers = {
			'Authorization': f'Bearer {access_token}'
		}
		movie_data = requests.get(f'http://localhost:8000/film/movies/{movie_id}/', headers=headers).json()
		return movie_data

	def get_access_token(self):
		token_url = "http://localhost:8000/o/token/"
		data = {
			'grant_type': 'client_credentials',
			'client_id': 'YOUR_CLIENT_ID',
			'client_secret': 'YOUR_CLIENT_SECRET',
			'scope': 'read'
		}
		response = requests.post(token_url, data=data)
		return response.json().get('access_token')