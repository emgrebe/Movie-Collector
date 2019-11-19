from django.db import models

class Movie(models.Model):
  title = models.CharField(max_length=100)
  year = models.IntegerField()
  description = models.TextField(max_length=150)

  def __str__(self):
    return self.title