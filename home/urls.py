from django.urls import path

from . import views

# Rotas do app home
urlpatterns = [
    path("", views.index, name="index"),
]
