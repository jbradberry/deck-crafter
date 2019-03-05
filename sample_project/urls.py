from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('deck_crafter/', include('deck_crafter.urls')),
    path('admin/', admin.site.urls),
]
