from django.shortcuts import render

class Movie:
  def __init__(self, title, year, actors, description):
    self.title = title
    self.year = year
    self.actors = actors
    self.description = description

movies = [
  Movie('Star Wars: A New Hope', 1977, 'Mark Hamill (Luke Skywalker), Harrison Ford (Han Solo), Carrie Fisher (Princess Leia), Alec Guinness (Obi-Wan Kenobi)', 'The first Star Wars movie made'),
  Movie('Star Wars: The Empire Strikes Back', 1980, 'Mark Hamill (Luke Skywalker), Harrison Ford (Han Solo), Carrie Fisher (Princess Leia), David Prowse (Darth Vader)', 'The second Star Wars movie made'),
  Movie('Star Wars: Return of The Jedi', 1983, 'Mark Hamill (Luke Skywalker), Harrison Ford (Han Solo), Carrie Fisher (Princess Leia), David Prowse (Darth Vader)', 'The third Star Wars movie made')
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
  return render(request, 'movies/index.html', { 'movies': movies })