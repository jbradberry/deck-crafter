from django.urls import path

from . import views


urlpatterns = [
    path('games/', views.GameListView.as_view()),
]
