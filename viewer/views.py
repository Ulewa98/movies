from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView

from viewer.forms import MovieForm, ActorForm
from viewer.models import Actor, Movie


class ActorsView(TemplateView):
    template_name = 'actors.html'
    extra_context = {'actors': Actor.objects.all()}


class MoviesView(TemplateView):
    template_name = 'movies.html'
    extra_context = {'movies': Movie.objects.all()}


class MovieCreateView(FormView):
    template_name = 'movie_create.html'
    form_class = MovieForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        Movie.objects.create(**form.cleaned_data)
        return result


class MovieUpdateView(UpdateView):
    template_name = 'movie_create.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('index')


class MovieDeleteView(DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('index')


class ActorCreateView(FormView):
    template_name = 'actor_create.html'
    form_class = ActorForm
    success_url = reverse_lazy('actors')

    def form_valid(self, form):
        result = super().form_valid(form)
        Actor.objects.create(**form.cleaned_data)
        return result


class ActorUpdateView(UpdateView):
    template_name = 'actor_create.html'
    form_class = ActorForm
    model = Actor
    success_url = reverse_lazy('actors')