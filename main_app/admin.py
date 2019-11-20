from django.contrib import admin
from .models import Movie, Watching, Review

admin.site.register(Movie)
admin.site.register(Watching)
admin.site.register(Review)