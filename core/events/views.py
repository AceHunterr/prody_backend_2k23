from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import generics
from .models import Event, Team
from .serializers import EventSerializer, TeamSerializer, EventRegistrationSerializer
from accounts.models import CustomUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


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


@api_view(['POST'])
def register_event(request, event_id):
    if request.method == 'POST':
        serializer = EventRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            try:
                user = CustomUser.objects.get(user_id=user_id)
                event = Event.objects.get(id=event_id)
                if user.registered_events.filter(id=event_id).exists():
                    return Response({'error': 'User is already registered for this event'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    user.registered_events.add(event)
                    # Update the registered_users field of the event
                    event.registered_users.add(user)
                    return Response({'message': 'Event registered successfully'}, status=status.HTTP_201_CREATED)
            except CustomUser.DoesNotExist:
                return Response({'error': 'User with provided user_id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            except Event.DoesNotExist:
                return Response({'error': 'Event with provided event_id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def register_team(request, team_id):
    if request.method == 'POST':
        serializer = EventRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            try:
                user = CustomUser.objects.get(user_id=user_id)
                team = Team.objects.get(id=team_id)
                if user.registered_teams.filter(id=team_id).exists():
                    return Response({'error': 'User is already registered for this event'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    user.registered_teams.add(team)
                    # Update the registered_users field of the event
                    team.registered_users.add(user)
                    return Response({'message': 'Event registered successfully'}, status=status.HTTP_201_CREATED)
            except CustomUser.DoesNotExist:
                return Response({'error': 'User with provided user_id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            except Team.DoesNotExist:
                return Response({'error': 'Event with provided event_id does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
