from django.contrib import admin

from .models import Game
from .models import Edition
from .models import Card

admin.site.register(Game)
admin.site.register(Edition)
admin.site.register(Card)
