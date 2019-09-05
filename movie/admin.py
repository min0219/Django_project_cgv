from django.contrib import admin

# Register your models here.
from .models import Region, Theater, Movie, Time

admin.site.register(Region)
admin.site.register(Theater)
admin.site.register(Movie)
admin.site.register(Time)