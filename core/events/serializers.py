from rest_framework import serializers
from .models import Event, Team
import random


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'event', 'members']

    def create(self, validated_data):
        members_data = validated_data.pop(
            'members', [])  # Extract members data

        # # Generate unique team ID
        # team_id = self.generate_unique_team_id()

        # # Add the generated team_id to the validated data
        # validated_data['team_id'] = team_id

        team = Team.objects.create(**validated_data)

        # Add members to the team
        team.members.set(members_data)

        return team

    def generate_unique_team_id(self):
        return f'#PDTM{random.randint(100000, 999999)}'


class EventRegistrationSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=12)
