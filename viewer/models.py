from django.db import models

from django.db.models import CharField, Model, DateField, FloatField, ForeignKey, IntegerField, TextField, \
    DateTimeField, DO_NOTHING


class Genre(Model):
  name = CharField(max_length=128)

class Actor(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    phone = CharField(max_length=20)
    email = CharField(max_length=100)
    salary = FloatField(default=10000)
class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)