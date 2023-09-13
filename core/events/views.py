from rest_framework import generics
from .models import Event, Team
from .serializers import EventSerializer, TeamSerializer
from accounts.models import CustomUser


class EventListView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class TeamView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)

    #     # Extract the team from the response data
    #     team = response.data
    #     print(response.data)

    #     # Get the list of member IDs
    #     member_ids = team.get('members', [])

    #     # Fetch user information for each member
    #     members_data = []
    #     for member_id in member_ids:
    #         try:
    #             user = CustomUser.objects.get(id=member_id)
    #             members_data.append({
    #                 'user_id': user.user_id,
    #                 # Add other user information you want to include
    #             })
    #         except CustomUser.DoesNotExist:
    #             pass

    #     response.data = {
    #         # 'team_id': team['team_id'],
    #         'members': members_data,
    #     }

    #     return response


class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
