from django.utils.html import escape
from rest_framework import generics
from rest_framework.response import Response

from .models import Robot, PitScout, Match, InGame, EndGame
from .serializers import RobotSerializer, PitScoutSerializer, MatchSerializer


class RobotList(generics.ListAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class MatchList(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchDetail(generics.ListAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

