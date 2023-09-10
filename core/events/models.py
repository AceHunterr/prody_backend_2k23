from django.db import models
from django.conf import settings
# Assuming 'CustomUser' is the correct model name
from accounts.models import CustomUser


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    abstract_link = models.URLField()
    poster = models.ImageField(upload_to='posters/')
    date_time = models.DateTimeField()
    registered_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='events_registered', blank=True)
    is_live = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_team_event = models.BooleanField(default=False)
    registered_teams = models.ManyToManyField(
        'Team', related_name='events_registered', blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='teams', blank=True)

    def __str__(self):
        return self.name
