from django.urls import path
from .views import EventListView, EventDetailView, TeamView, TeamDetailView, register_event

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('teams/', TeamView.as_view(), name='team-list'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('register_event/<int:event_id>/',
         register_event, name='register_event'),

]
