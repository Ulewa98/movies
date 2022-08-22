"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.models import Genre, Actor, Movie
from viewer.views import MoviesView, ActorsView, MovieCreateView, ActorCreateView, MovieUpdateView

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('actors/', ActorsView.as_view(), name='actors'),
    path('actors/create', ActorCreateView.as_view()),

    path("", MoviesView.as_view(), name='index'),
    path('movies/', MoviesView.as_view()),
    path('movie/create', MovieCreateView.as_view(), name='movie_create'),
    path('movie/update/<pk>', MovieUpdateView.as_view()),
    path('movie/', MoviesView.as_view())
]

