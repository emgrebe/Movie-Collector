from django.db import models
from django.urls import reverse

TIMES = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('E', 'Evening')
)

class Movie(models.Model):
  title = models.CharField(max_length=100)
  year = models.IntegerField()
  description = models.TextField(max_length=150)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={ 'movie_id': self.id })

class Watching(models.Model):
  date = models.DateField('watch date')
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