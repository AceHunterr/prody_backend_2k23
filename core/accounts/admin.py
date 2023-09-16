from django.contrib import admin
from .models import CustomUser
from import_export.admin import ImportExportModelAdmin
from .resources import CustomUserResource


class CustomUserAdmin(ImportExportModelAdmin):
    resource_class = CustomUserResource
    list_display = ('username', 'email', 'user_id', 'get_registered_events')

    def get_registered_events(self, obj):
        return ", ".join([event.name for event in obj.registered_events.all()])

    get_registered_events.short_description = 'Registered Events'

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        # Get the updated set of registered events after saving
        updated_registered_events = set(form.instance.registered_events.all())

        # Find events that were removed from registration
        removed_events = set(
            form.initial['registered_events']) - updated_registered_events

        # Find events that were added to registration
        added_events = updated_registered_events - \
            set(form.initial['registered_events'])

        # Remove user from removed events' registered_users
        for event in removed_events:
            event.registered_users.remove(form.instance)

        # Add user to added events' registered_users
        for event in added_events:
            event.registered_users.add(form.instance)


admin.site.register(CustomUser, CustomUserAdmin)
