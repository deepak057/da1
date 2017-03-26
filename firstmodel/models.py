from django.db import models
from django.utils import timezone

# Create your models here.


class Mybasicmodel(models.Model):
	email=models.EmailField(unique=True)
	something=models.CharField(max_length=100, blank=True)
	
	def save_method(self, email, something='Anything'):
		
		if not email:
			raise ValueError ("You must enter an email")
		self.email=email
		self.something=something
		self.save()
		