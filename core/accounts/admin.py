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


admin.site.register(CustomUser, CustomUserAdmin)
