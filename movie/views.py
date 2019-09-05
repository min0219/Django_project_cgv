from django.shortcuts import render
from django.http import HttpResponse
from .models import Region, Theater, Movie

# Create your views here.

def main(request):
	regions = Region.objects.all()
	return render(request, 'main.html', {'regions':regions})
	
def region_theaters(request, pk):
	region = Region.objects.get(pk=pk)
	key = region.region_name
	theaters = Theater.objects.filter(region_name2__region_name = key)
	return render(request, 'theater.html', {'region': region ,'theaters': theaters})

def theater_movies(request, pk):
	theater = Theater.objects.get(pk=pk)
	movies = Movie.objects.all()
	return render(request, 'movie.html', { 'theater': theater, 'movies': movies })
