from django.db import models

# Create your models here.
class Region(models.Model):
	region_name = models.CharField(max_length = 30, unique = True)

	def __str__(self):
		return self.region_name

class Theater(models.Model):
	region_name2 = models.ForeignKey(Region, on_delete = models.CASCADE)
	theater_name = models.CharField(max_length = 30)

	def __str__(self):
		return self.theater_name

class Movie(models.Model):
	movie_name = models.CharField(max_length=30)
	image = models.ImageField(upload_to='%Y/%m/%d/orig')

	def __str__(self):
		return self.movie_name

class Time(models.Model):
	time = models.CharField(max_length=30)
	seat = models.IntegerField(default = 200)

	def __str__(self):
		return self.time

