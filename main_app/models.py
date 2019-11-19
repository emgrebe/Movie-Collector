from django.db import models
from django.urls import reverse

class Movie(models.Model):
  title = models.CharField(max_length=100)
  year = models.IntegerField()
  description = models.TextField(max_length=150)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={ 'movie_id': self.id })