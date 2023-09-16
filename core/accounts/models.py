from django.contrib.auth.models import AbstractUser
from django.db import models
import random
# from events.models import Event, Team


def generate_default_user_id():
    return f'#PY{random.randint(100000000, 999999999)}'


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_id = models.CharField(
        max_length=12, unique=True, default=generate_default_user_id)
    registered_events = models.ManyToManyField(
        'events.Event', related_name='reg_users', blank=True)
    registered_teams = models.ManyToManyField(
        'events.Team', related_name='reg_users_teams', blank=True)

    def __str__(self):
        return f'{self.username} - {self.user_id}'

    def register_for_event(self, event):
        self.registered_events.add(event)

    def register_for_team(self, team):
        self.registered_teams.add(team)

    def clear_registered_events(self):
        for event in self.registered_events.all():
            event.registered_users.remove(self)

    # def save(self, *args, **kwargs):
    #     # Get the initial set of registered events before saving
    #     initial_registered_events = set(self.registered_events.all())
    #     print(f"initial_registered_events {initial_registered_events}")
    #     super().save(*args, **kwargs)

    #     # Get the updated set of registered events after saving
    #     updated_registered_events = set(self.registered_events.all())
    #     print(f"updated_registered_events {updated_registered_events}")
    #     # Find events that were removed from registration
    #     removed_events = initial_registered_events - updated_registered_events
    #     print(f"removed_events {removed_events}")
    #     # Find events that were added to registration
    #     added_events = updated_registered_events - initial_registered_events

    #     # Remove user from removed events' registered_users
    #     for event in removed_events:

    #         print(event.registered_users.all)
    #         event.registered_users.remove(self)
    #         print(event.registered_users.all())

    #     # Add user to added events' registered_users
    #     for event in added_events:
    #         event.registered_users.add(self)
