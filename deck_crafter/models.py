from django.db import models
from django.contrib.postgres.fields import ArrayField

from sorl.thumbnail import ImageField


class Game(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    image = ImageField(upload_to='games', null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Edition(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    image = ImageField(upload_to='editions', null=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    tags = ArrayField(
        models.CharField(max_length=64),
        help_text="Use a comma to separate tags in the edit form field.",
    )
    text = models.TextField()
    image = ImageField(upload_to='cards', null=True)
    artist = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name
