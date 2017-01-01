from django.db import models
import re

class Poster(models.Model):
	title = models.CharField(max_length=200,  null=True)
	image =  models.CharField(max_length=200,  null=True)
	year = models.CharField(max_length=200,  null=True)
	genre = models.CharField(max_length=200,  null=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["year"]

