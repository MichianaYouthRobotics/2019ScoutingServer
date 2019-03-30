import json

from django.http import JsonResponse, HttpResponse
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Sum, Avg, Count
from django.db.models.functions import Coalesce
from django.template.loader import get_template
from weasyprint import HTML, CSS



from .models import Robot, PitScout, MatchScout, Event, CoachScout
from .serializers import RobotSerializer, PitScoutSerializer, MatchScoutSerializer, EventSerializer, \
    CoachScoutSerializer, RobotAnalyzeSerializer


class RobotList(generics.ListAPIView):
    serializer_class = RobotSerializer

    def get_queryset(self):
        event = self.kwargs['event']
        robots = Event.objects.get(id=event).robots.all()
        return robots


class TopHatchRobotList(generics.ListAPIView):
    serializer_class = RobotAnalyzeSerializer

    def get_queryset(self):
        best_bots = Robot.objects.annotate(total=Coalesce(Sum('matchscout__hatch_count'), -1), avg=Coalesce(Avg('matchscout__hatch_count'), -1)).order_by('-avg')
        return best_bots


class TopCargoRobotList(generics.ListAPIView):
    serializer_class = RobotAnalyzeSerializer

    def get_queryset(self):
        best_bots = Robot.objects.annotate(total=Coalesce(Sum('matchscout__cargo_count'), -1), avg=Coalesce(Avg('matchscout__cargo_count'), -1)).order_by('-avg')
        return best_bots


class TopClimbRobotList(generics.ListAPIView):
    serializer_class = RobotAnalyzeSerializer

    def get_queryset(self):
        best_bots = Robot.objects.annotate(total=Coalesce(Sum('matchscout__hab_level_int'), -1), avg=Coalesce(Avg('matchscout__hab_level_int'), -1)).order_by('-avg')
        return best_bots


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
def fix_hab_levels(request):
    all_match_scouts = MatchScout.objects.all()
    for match_scout in all_match_scouts:
        match_scout.hab_level_int = int(match_scout.hab_level)
        match_scout.save()
    return JsonResponse({'status': 'OK'})


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




@csrf_exempt
def sync_pit_scouts(request, event_id):
    if request.method == 'POST':
        body = json.loads(request.body)
        key = body.get('key')
        try:
            event = Event.objects.get(id=event_id, event_key=key)
            unique_scout_key = body.get('unique_scout_key')
            robot_number = body.get('robot').get('robot_number')
            robot = Robot.objects.get(robot_number=robot_number)
            snow_days = body.get('snow_days')
            starts_on_hab_2 = body.get('starts_on_hab_2')
            cargo_in_sandstorm = body.get('cargo_in_sandstorm')
            hatches_in_sandstorm = body.get('hatches_in_sandstorm')
            cargo_in_teleop = body.get('cargo_in_teleop')
            hatches_in_teleop = body.get('hatches_in_teleop')
            climb_level = body.get('climb_level')
            max_rocket_height = body.get('max_rocket_height')
            ground_pickup_cargo = body.get('ground_pickup_cargo')
            ground_pickup_hatch = body.get('ground_pickup_hatch')
            favorite_feature = body.get('favorite_feature')
            notes = body.get('noes')
            rating = body.get('rating')
            do_not_pick = body.get('do_not_pick')
            scouter = body.get('scouter')
            buddy_climb = body.get('buddy_climb')
            if PitScout.objects.filter(unique_scout_key=unique_scout_key).count() < 1:
                new_pit_scout = PitScout.objects.create(
                    event=event, unique_scout_key=unique_scout_key, snow_days=snow_days, starts_on_hab_2=starts_on_hab_2,
                    robot=robot, cargo_in_sandstorm=cargo_in_sandstorm, hatches_in_sandstorm=hatches_in_sandstorm,
                    cargo_in_teleop=cargo_in_teleop, hatches_in_teleop=hatches_in_teleop, climb_level=climb_level,
                    max_rocket_height=max_rocket_height, ground_pickup_cargo=ground_pickup_cargo,
                    ground_pickup_hatch=ground_pickup_hatch, favorite_feature=favorite_feature, notes=notes, rating=rating,
                    do_not_pick=do_not_pick, scouter=scouter, buddy_climb=buddy_climb,
                )
                new_pit_scout.save()
            return JsonResponse({'status': 'OK'})
        except Event.DoesNotExist:
            return JsonResponse({'error': 'bad EVENT ID or KEY'})
    return JsonResponse({'error': 'POST requests only'})


@csrf_exempt
def sync_match_scouts(request, event_id):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            key = body.get('key')
            event = Event.objects.get(id=event_id, event_key=key)

            unique_scout_key = body.get('unique_scout_key')
            scouter = body.get('scouter')
            robot_number = body.get('robot').get('robot_number')
            robot = Robot.objects.get(robot_number=robot_number)

            alliance = body.get('alliance')
            match_number = body.get('match_number')
            start_position = body.get('start_position')
            hab_level = body.get('hab_level')
            speed = body.get('speed')
            strategy = body.get('strategy')
            team_work = body.get('team_work')
            recommend = body.get('recommend')
            notes = body.get('notes')
            in_match_actions = body.get('in_match_actions')
            hatch_count = body.get('hatch_count')
            cargo_count = body.get('cargo_count')
            if MatchScout.objects.filter(unique_scout_key=unique_scout_key).count() < 1:
                new_match_scout = MatchScout.objects.create(
                    robot=robot, event=event, unique_scout_key=unique_scout_key, scouter=scouter, alliance=alliance,
                    match_number=match_number, start_position=start_position, hab_level=hab_level, speed=speed,
                    strategy=strategy, team_work=team_work, recommend=recommend, notes=notes, in_match_actions=in_match_actions,
                    hatch_count=hatch_count, cargo_count=cargo_count
                )

                new_match_scout.save()
            return JsonResponse({'status': 'OK'})

        except Event.DoesNotExist:
            return JsonResponse({'error': 'bad EVENT ID or KEY'})

    return JsonResponse({'error': 'POST requests only'})


@csrf_exempt
def sync_coach_scouts(request, event_id):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            key = body.get('key')
            event = Event.objects.get(id=event_id, event_key=key)
            unique_scout_key = body.get('unique_scout_key')
            scouter = body.get('scouter')

            robot_number = body.get('robot').get('robot_number')
            robot = Robot.objects.get(robot_number=robot_number)

            match_number = body.get('match_number')
            synergy = body.get('synergy')
            notes = body.get('notes')

            if CoachScout.objects.filter(unique_scout_key=unique_scout_key).count() < 1:
                new_coach_scout = CoachScout.objects.create(
                    robot=robot, event=event, unique_scout_key=unique_scout_key, scouter=scouter, match_number=match_number,
                    synergy=synergy, notes=notes
                )
                new_coach_scout.save()

            return JsonResponse({'status': 'OK'})

        except Event.DoesNotExist:
            return JsonResponse({'error': 'bad EVENT ID or KEY'})

    return JsonResponse({'error': 'POST requests only'})


def print_hatches(request, event_id):
    event = Event.objects.get(id=event_id)
    best_bots = event.robots.all().annotate(total_hatches=Coalesce(Sum('matchscout__hatch_count'), -1),
                                            avg_hatches=Coalesce(Avg('matchscout__hatch_count'), -1),
                                            total_cargo=Coalesce(Sum('matchscout__cargo_count'), -1),
                                            avg_cargo=Coalesce(Avg('matchscout__cargo_count'), -1),
                                            total_climb=Coalesce(Sum('matchscout__hab_level_int'), -1),
                                            avg_climb=Coalesce(Avg('matchscout__hab_level_int'), -1)
                                            ).order_by('-avg_hatches')
     # = Robot.objects.filter()
    template = get_template('print/hatches.html')
    html = template.render({'best_bots': best_bots})
    pdf_file = HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=hatchbots.pdf'
    return response

def print_cargo(request, event_id):
    event = Event.objects.get(id=event_id)
    best_bots = event.robots.all().annotate(total_hatches=Coalesce(Sum('matchscout__hatch_count'), -1),
                                            avg_hatches=Coalesce(Avg('matchscout__hatch_count'), -1),
                                            total_cargo=Coalesce(Sum('matchscout__cargo_count'), -1),
                                            avg_cargo=Coalesce(Avg('matchscout__cargo_count'), -1),
                                            total_climb=Coalesce(Sum('matchscout__hab_level_int'), -1),
                                            avg_climb=Coalesce(Avg('matchscout__hab_level_int'), -1)
                                            ).order_by('-avg_cargo')
     # = Robot.objects.filter()
    template = get_template('print/cargo.html')
    html = template.render({'best_bots': best_bots})
    pdf_file = HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=cargobots.pdf'
    return response

def print_climb(request, event_id):
    event = Event.objects.get(id=event_id)
    best_bots = event.robots.all().annotate(total_hatches=Coalesce(Sum('matchscout__hatch_count'), -1),
                                            avg_hatches=Coalesce(Avg('matchscout__hatch_count'), -1),
                                            total_cargo=Coalesce(Sum('matchscout__cargo_count'), -1),
                                            avg_cargo=Coalesce(Avg('matchscout__cargo_count'), -1),
                                            total_climb=Coalesce(Sum('matchscout__hab_level_int'), -1),
                                            avg_climb=Coalesce(Avg('matchscout__hab_level_int'), -1)
                                            ).order_by('-avg_climb')
     # = Robot.objects.filter()
    template = get_template('print/climb.html')
    html = template.render({'best_bots': best_bots})
    pdf_file = HTML(string=html).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=climbbots.pdf'
    return response
