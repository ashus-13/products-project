from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
	title = models.CharField(max_length=100)
	url =models.TextField()
	pub_date = models.DateTimeField()
	tvotes = models.IntegerField(default=1)
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')
	body = models.TextField()
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.title
		
	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')

	def summary(self):
		return self.body[:200]	
