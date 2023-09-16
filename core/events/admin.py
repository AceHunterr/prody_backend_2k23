from django.contrib import admin
from .models import Event, Team
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class EventAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description', 'abstract_link', 'date_time', 'is_live',
                    'is_completed', 'is_team_event')  # Customize as per your needs


admin.site.register(Event, EventAdmin)
admin.site.register(Team)
