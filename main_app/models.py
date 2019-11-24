from django.db import models
from django.urls import reverse
from datetime import date

TIMES = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('E', 'Evening')
)

RATINGS = (
  ('1', 'Do Not Watch Again'),
  ('2', 'Did Not Like It'),
  ('3', 'It Was Kinda Good'),
  ('4', 'I Liked It'),
  ('5', 'I Loved This Movie')
)

class Review(models.Model):
  comment = models.TextField(max_length=250)
  rating = models.IntegerField()

  def __str__(self):
    return self.rating

  def get_absolute_url(self):
    return reverse('reviews_detail', kwargs={'pk': self.id})

class Movie(models.Model):
  title = models.CharField(max_length=100)
  year = models.IntegerField()
  description = models.TextField(max_length=150)
  reviews = models.ManyToManyField(Review)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={ 'movie_id': self.id })

class Watching(models.Model):
  date = models.DateField('Watch Date')
  time = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0]
  )

  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_time_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for movie_id: {self.movie_id} @{self.url}"