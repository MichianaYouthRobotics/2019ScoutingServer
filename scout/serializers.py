from rest_framework import serializers

from .models import Robot, PitScout, MatchScout, Event, CoachScout


class RobotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Robot
        fields = ('robot_pk', 'robot_number', 'team_name', 'photo', 'location', 'favorite')


class PitScoutSerializer(serializers.ModelSerializer):
    robot = RobotSerializer(many=False)

    class Meta:
        model = PitScout
        fields = ('pit_scout_pk', 'robot', 'snow_days', 'starts_on_hab_2', 'cargo_in_sandstorm', 'hatches_in_sandstorm',
                  'cargo_in_teleop', 'hatches_in_teleop', 'climb_level', 'max_rocket_height', 'ground_pickup_cargo',
                  'ground_pickup_hatch', 'favorite_feature', 'notes', 'rating', 'do_not_pick', 'scouter')


class MatchScoutSerializer(serializers.ModelSerializer):
    robot = RobotSerializer(many=False)

    class Meta:
        model = MatchScout
        fields = ('match_pk', 'scouter', 'robot', 'alliance', 'match_number', 'event_date', 'in_match_actions',
                  'hatch_count', 'cargo_count', 'speed', 'hab_level', 'start_position', 'strategy', 'team_work',
                  'in_match_actions', 'notes')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'name', 'event_key', 'location', 'week_number', 'start_date', 'end_date')


class CoachScoutSerializer(serializers.ModelSerializer):
    robot = RobotSerializer()

    class Meta:
        model = CoachScout
        fields = ('id', 'robot', 'event', 'match_number', 'synergy', 'notes', 'scouter')
