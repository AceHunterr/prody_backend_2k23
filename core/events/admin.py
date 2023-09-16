from django.contrib import admin
from .models import Event, Team
from import_export.admin import ImportExportModelAdmin


class EventAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'get_registered_users')

    def get_registered_users(self, obj):
        return ", ".join([user.username for user in obj.registered_users.all()])

    get_registered_users.short_description = 'Registered Users'

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        # Get the updated set of registered users after saving
        updated_registered_users = set(form.instance.registered_users.all())

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


admin.site.register(Event, EventAdmin)
admin.site.register(Team)
