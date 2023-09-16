from import_export import resources
from .models import CustomUser


class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_id', 'registered_events')
