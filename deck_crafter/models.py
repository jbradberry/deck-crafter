from django.db import models
from django.contrib.postgres.fields import ArrayField


class Game(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(null=True)


class Edition(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(null=True)


class Card(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    tags = ArrayField(models.CharField(max_length=64))
    text = models.TextField()
    image = models.ImageField(null=True)
    artist = models.CharField(max_length=256, blank=True)
