from rest_framework import serializers

from .models import Robot, PitScout, Match, InGame, EndGame


class RobotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Robot
        fields = ('robot_pk', 'robot_number', 'team_name', 'photo')


class PitScoutSerializer(serializers.ModelSerializer):
    robot = RobotSerializer(many=False)

    class Meta:
        model = PitScout
        fields = ('pit_scout_pk', 'robot', 'snow_days', 'starts_on_hab_2', 'cargo_in_sandstorm', 'cargo_in_teleop',
                  'hatches_in_teleop', 'climb_level', 'max_rocket_height', 'ground_pickup_cargo', 'ground_pickup_hatch',
                  'favorite_features', 'notes', 'rating', 'do_not_pick')


class InGameSerializer(serializers.ModelSerializer):

    class Meta:
        model = InGame
        fields = ('in_game_pk', 'action', 'seconds')


class EndGameSerializer(serializers.ModelSerializer):

    class Meta:
        model = EndGame
        fields = ('speed', 'hab_level')


class MatchSerializer(serializers.ModelSerializer):
    robot = RobotSerializer(many=False)
    in_game_actions = InGameSerializer(many=True)
    end_game = EndGameSerializer(many=False)

    class Meta:
        model = Match
        fields = ('match_pk', 'scouter', 'robot', 'match_number', 'event_date', 'in_game_actions', 'end_game')
