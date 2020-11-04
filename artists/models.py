from django.db import models


class State(models.Model):
  uf_code = models.IntegerField()
  name = models.CharField(max_length=80)
  uf = models.CharField(max_length=2)
  region = models.IntegerField()

  def __str__(self):
    return self.uf

class Tag(models.Model):
  name = models.CharField(max_length=60)
  description = models.CharField(max_length=200, null=True, blank=True)

  def __str__(self):
    return self.name

class Artist(models.Model):
  name = models.CharField(max_length=80)
  contact = models.CharField(max_length=200, null=True, blank=True)
  instagram_username = models.CharField(max_length=80, null=True, blank=True)
  portfolio = models.CharField(max_length=200)
  state = models.ForeignKey(State, null=True, blank=True, on_delete=models.SET_NULL)
  tags = models.ManyToManyField(Tag, blank=True)

  def __str__(self):
    return self.name