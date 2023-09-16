# core/accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin

# import csv
# import json


# def export_users_as_csv(modeladmin, request, queryset):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="users.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['Username', 'Email', 'User ID'])

#     for user in queryset:
#         writer.writerow([user.username, user.email, user.user_id])

#     return response


# def export_users_as_json(modeladmin, request, queryset):
#     response = HttpResponse(content_type='application/json')
#     response['Content-Disposition'] = 'attachment; filename="users.json"'

#     users = [{'username': user.username, 'email': user.email,
#               'user_id': user.user_id} for user in queryset]

#     response.write(json.dumps(users))


# export_users_as_csv.short_description = "Export selected users as CSV"
# export_users_as_json.short_description = "Export selected users as JSON"


class CustomUserAdmin(ImportExportModelAdmin):
    # actions = [export_users_as_csv, export_users_as_json]
    list_display = ('username', 'email', 'user_id', 'get_registered_events')

    def get_registered_events(self, obj):
        return ", ".join([event.name for event in obj.registered_events.all()])

    get_registered_events.short_description = 'Registered Events'


admin.site.register(CustomUser, CustomUserAdmin)
