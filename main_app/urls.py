from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('movies/', views.movies_index, name='index'),
  path('movies/<int:movie_id>/', views.movies_detail, name='detail'),
  path('movies/create/', views.MovieCreate.as_view(), name='movies_create'),
  path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movies_update'),
  path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movies_delete'),
  path('movies/<int:movie_id>/add_watching/', views.add_watching, name='add_watching'),
  path('reviews/', views.ReviewList.as_view(), name='reviews_index'),
  path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='reviews_detail'),
  path('reviews/create', views.ReviewCreate.as_view(), name='reviews_create'),
  path('reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='reviews_update'),
  path('reviews/<int:pk>/delete/', views.ReviewDelete.as_view(), name='reviews_delete'),
]