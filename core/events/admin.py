from django.contrib import admin
from .models import Event, Team
from import_export.admin import ImportExportModelAdmin


class EventAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'get_registered_users',
                    'get_registered_teams')

    def get_registered_users(self, obj):
        return ", ".join([user.username for user in obj.registered_users.all()])

    def get_registered_teams(self, obj):
        return ", ".join([team.name for team in obj.registered_teams.all()])

    get_registered_users.short_description = 'Registered Users'
    get_registered_teams.short_description = 'Registered Teams'

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        if change:
            updated_registered_users = set(
                form.instance.registered_users.all())

            removed_users = set(
                form.initial['registered_users']) - updated_registered_users

            added_users = updated_registered_users - \
                set(form.initial['registered_users'])

            for user in removed_users:
                user.registered_events.remove(form.instance)

            for user in added_users:
                user.registered_events.add(form.instance)

            updated_registered_teams = set(
                form.instance.registered_teams.all())
            print(f"updated_registered_teams {updated_registered_teams}")
            removed_teams = set(
                form.initial['registered_teams']) - updated_registered_teams
            print(
                f"set(form.initial['registered_teams']) {set(form.initial['registered_teams'])}")
            print(f"removed_teams {removed_teams}")
            added_teams = updated_registered_teams - \
                set(form.initial['registered_teams'])

            for team in removed_teams:
                team.event = None
                team.save()

            for team in added_teams:
                team.event = form.instance
                team.save()


class TeamAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'team_id', 'get_registered_users', 'event')

    def get_registered_users(self, obj):
        return ", ".join([user.username for user in obj.registered_users.all()])

    get_registered_users.short_description = 'Registered Users'

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        if change:
            # Get the updated set of registered users after saving
            updated_registered_users = set(
                form.instance.registered_users.all())
            print(" updated users", updated_registered_users)
            # Find users that were removed from registration
            removed_users = set(
                form.initial['registered_users']) - updated_registered_users

            # Find users that were added to registration
            added_users = updated_registered_users - \
                set(form.initial['registered_users'])
            print(f"added_users {added_users}")
            # Remove event from removed users' registered_teams
            for user in removed_users:
                user.registered_teams.remove(form.instance)

            # Add event to added users' registered_teams
            for user in added_users:
                user.registered_teams.add(form.instance)

            # Check if there's an associated event
            if form.instance.event:
                # Remove team from removed event's registered_teams
                removed_event = set([form.instance.event])
                for event in removed_event:
                    event.registered_teams.remove(form.instance)

                # Add team to added event's registered_teams
                added_event = set([form.cleaned_data['event']])
                for event in added_event:
                    event.registered_teams.add(form.instance)


admin.site.register(Event, EventAdmin)
admin.site.register(Team, TeamAdmin)
