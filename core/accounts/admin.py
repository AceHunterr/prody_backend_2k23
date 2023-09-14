from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_id',
                    'get_registered_events', 'get_team_in_event')

    def get_registered_events(self, obj):
        return ", ".join([event.name for event in obj.events_registered.all()])

    def get_team_in_event(self, obj):
        return ", ".join([team.name for team in obj.teams.all()])

    get_registered_events.short_description = 'Registered Events'
    get_team_in_event.short_description = 'Team in Event'


# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
