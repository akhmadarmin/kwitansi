from django.contrib.auth.models import User

class MovieData(models.Model):
	name = models.CharField(max_length=200)
	duration = models.FloatField()
	rating = models.FloatField()
	typ = models.CharField(max_length=200, default='action')
	image = models.ImageField(upload_to='Image/', default='Images/None/Noimg.jpg')

	def __str__(self):
		return self.name
	
class Review(models.Model):
	movie = models.ForeignKey(MovieData, on_delete=models.CASCADE, related_name='reviews')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField()
	rating = models.FloatField()

	def __str__(self):
		return f"Review for {self.movie.name} by {self.user.username}"