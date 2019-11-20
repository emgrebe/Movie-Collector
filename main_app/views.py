from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import  DetailView, ListView
from .models import Movie, Review
from .forms import WatchingForm

class MovieCreate(CreateView):
  model = Movie
  fields = '__all__'

class MovieUpdate(UpdateView):
  model = Movie
  fields = ['year', 'description']

class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
  movies = Movie.objects.all()
  return render(request, 'movies/index.html', { 'movies': movies })

def movies_detail(request, movie_id):
  movie = Movie.objects.get(id=movie_id)
  watching_form = WatchingForm()
  return render(request, 'movies/detail.html', { 
    'movie': movie, 'watching_form': watching_form 
  })

def add_watching(request, movie_id):
  form = WatchingForm(request.POST)
  if form.is_valid():
    new_watching = form.save(commit=False)
    new_watching.movie_id = movie_id
    new_watching.save()
  return redirect('detail', movie_id=movie_id)

class ReviewList(ListView):
  model = Review

class ReviewDetail(DetailView):
  model = Review

class ReviewCreate(CreateView):
  model = Review
  fields='__all__'

class ReviewUpdate(UpdateView):
  model = Review
  fields = ['rating', 'comment']

class ReviewDelete(DeleteView):
  modle = Review
  success_url = '/reviews/'