from django.contrib import admin
from .models import Event, Team
from import_export.admin import ImportExportModelAdmin


class EventAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'get_registered_users')

    def get_registered_users(self, obj):
        return ", ".join([user.username for user in obj.registered_users.all()])

    get_registered_users.short_description = 'Registered Users'


admin.site.register(Event, EventAdmin)
admin.site.register(Team)
