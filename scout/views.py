import json

from django.http import JsonResponse
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.response import Response

from .models import Robot, PitScout, MatchScout, Event, CoachScout
from .serializers import RobotSerializer, PitScoutSerializer, MatchScoutSerializer, EventSerializer, CoachScoutSerializer


class RobotList(generics.ListAPIView):
    serializer_class = RobotSerializer

    def get_queryset(self):
        event = self.kwargs['event']
        robots = Event.objects.get(id=event).robots.all()
        return robots


class PitScouts(generics.ListAPIView):
    serializer_class = PitScoutSerializer

    def get_queryset(self):
        event = self.kwargs['event']
        return PitScout.objects.filter(event__id=event)


class MatchScouts(generics.ListAPIView):
    serializer_class = MatchScoutSerializer

    def get_queryset(self):
        event = self.kwargs['event']
        return MatchScout.objects.filter(event__id=event)


class CoachScouts(generics.ListAPIView):
    serializer_class = CoachScoutSerializer

    def get_queryset(self):
        event = self.kwargs['event']
        return CoachScout.objects.filter(event__id=event)


@csrf_exempt
def event_login(request, pk):
    if request.method == 'POST':
        body = json.loads(request.body)
        key = body.get('key')
        try:
            print(key)
            event = Event.objects.get(id=pk, event_key=key)
            print('here!')

            serialized = EventSerializer(event)
            print(serialized.data)
            return JsonResponse(serialized.data)
        except Event.DoesNotExist:
            return JsonResponse({'error': 'bad EVENT ID or KEY'})
    return JsonResponse({'error': 'POST requests only'})


@csrf_exempt
def sync(request, pk):
    if request.method == 'POST':
        body = json.loads(request.body)
        key = body.get('key')
        scouts = body.get('scouts')
        try:
            event = Event.objects.get(id=pk, event_key=key)

            serialized = EventSerializer(event)
            print(serialized.data)
            return JsonResponse(serialized.data)
        except Event.DoesNotExist:
            return JsonResponse({'error': 'bad EVENT ID or KEY'})
    return JsonResponse({'error': 'POST requests only'})




