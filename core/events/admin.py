from django.contrib import admin
from .models import Event, Team
from import_export.admin import ImportExportModelAdmin


class EventAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'get_registered_users')

    def get_registered_users(self, obj):
        return ", ".join([user.username for user in obj.registered_users.all()])

    get_registered_users.short_description = 'Registered Users'

    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)
    #     print(f"Change: {change}")

    #     # This block of code will only be executed if the event is being altered
    #     if change:
    #         updated_registered_users = set(obj.registered_users.all())
    #         print(f"updated_registered_users {updated_registered_users}")
    #         # Find users that were removed from registration
    #         removed_users = set(
    #             form.initial['registered_users']) - updated_registered_users
    #         print(
    #             f"set(form.initial['registered_users']) {set(form.initial['registered_users'])}")
    #         print(f"removed_users {removed_users}")
    #         # Find users that were added to registration
    #         added_users = updated_registered_users - \
    #             set(form.initial['registered_users'])

    #         # Remove event from removed users' registered_events
    #         for user in removed_users:
    #             user.reg_users.remove(obj)

    #         # Add event to added users' registered_events
    #         for user in added_users:
    #             user.reg_users.add(obj)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        if change:
            print(f"change : {change}")
            # Get the updated set of registered users after saving
            updated_registered_users = set(
                form.instance.registered_users.all())

            # Find users that were removed from registration
            removed_users = set(
                form.initial['registered_users']) - updated_registered_users

            # Find users that were added to registration
            added_users = updated_registered_users - \
                set(form.initial['registered_users'])

            # Remove event from removed users' registered_events
            for user in removed_users:
                user.registered_events.remove(form.instance)

            # Add event to added users' registered_events
            for user in added_users:
                user.registered_events.add(form.instance)


class TeamAdmin(ImportExportModelAdmin):
    list_display = ('team_id', 'name', 'get_registered_users')

    def get_registered_users(self, obj):
        return ", ".join([user.username for user in obj.registered_users.all()])

    get_registered_users.short_description = 'Registered Users'

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        # Get the updated set of registered users after saving
        updated_registered_users = set(form.instance.registered_users.all())
        print(updated_registered_users)
        print(set(form.initial))
        # Find users that were removed from registration
        removed_users = set(
            form.initial['registered_users']) - updated_registered_users

        # Find users that were added to registration
        added_users = updated_registered_users - \
            set(form.initial['registered_users'])

        # Remove event from removed users' registered_events
        for user in removed_users:
            user.registered_teams.remove(form.instance)

        # Add event to added users' registered_events
        for user in added_users:
            user.registered_teams.add(form.instance)


admin.site.register(Event, EventAdmin)
admin.site.register(Team, TeamAdmin)
