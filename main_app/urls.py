from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('movies/', views.movies_index, name='index'),
  path('movies/<int:movie_id>/', views.movies_detail, name='detail'),
  path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
]