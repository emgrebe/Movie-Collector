from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WatchingForm, ReviewForm
from .models import Movie, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'moviecollect'

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
  review_form = ReviewForm()
  watching_form = WatchingForm()
  return render(request, 'movies/detail.html', { 
    'movie': movie, 'watching_form': watching_form,
    'review_form': review_form
  })

def add_watching(request, movie_id):
  form = WatchingForm(request.POST)
  if form.is_valid():
    new_watching = form.save(commit=False)
    new_watching.movie_id = movie_id
    new_watching.save()
  return redirect('detail', movie_id=movie_id)

def add_review(request, movie_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.movie_id = movie_id
    new_review.save()
  return redirect('detail', movie_id=movie_id)

def add_photo(request, movie_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, movie_id=movie_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', movie_id=movie_id)