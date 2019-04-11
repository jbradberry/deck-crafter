from django.views import generic

from . import models


class GameListView(generic.ListView):
    model = models.Game
    paginate_by = 20
