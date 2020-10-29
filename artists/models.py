from django.db import models

# Create your models here.
class States(models.Model):
  uf_code = models.IntegerField()
  name = models.CharField(max_length=80)
  uf = models.CharField(max_length=2)
  region = models.IntegerField()

  def __str__(self):
    return self.name

class Artist(models.Model):
  name = models.CharField(max_length=80)
  instagram_url = models.CharField(max_length=200)
  instagram_username = models.CharField(max_length=80)
  url = models.CharField(max_length=200)
  state = models.ForeignKey(States, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return self.name

class Tags(models.Model):
  name = models.CharField(max_length=60)
  artists = models.ManyToManyField(Artist)

  def __str__(self):
    return self.name
  