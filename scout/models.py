import random
from django.db import models



def random_words():
    adj = ('SCRATCHY', 'SPEEDY', 'ELECTRIC', 'POWERFUL', 'OVERPOWERED', 'GREEN', 'BLACK')
    noun = ('ROBOT', 'AI', 'PC', 'SERVER', 'CAT', 'TRAIN', 'CLOUD')
    return f'{random.choice(adj)}-{random.choice(noun)}'


class Event(models.Model):
    name = models.CharField(max_length=255)
    event_key = models.CharField(max_length=55, default=random_words)
    location = models.CharField(max_length=255)
    week_number = models.IntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    robots = models.ManyToManyField('Robot', blank=True)


class Robot(models.Model):
    robot_number = models.IntegerField(default=0, unique=True)
    team_name = models.CharField(max_length=100,blank=True, null=True)
    location = models.CharField(max_length=100, default='')
    photo = models.ImageField(blank=True, null=True)
    favorite = models.BooleanField(default=False)


    @property
    def robot_pk(self):
        return f'robot_{self.id}'

    def __str__(self):
        return f'{self.robot_number} - {self.team_name}'

    class Meta:
        ordering = ['robot_number']


class PitScout(models.Model):
    SANDSTORM_CHOICES = (
        ('n', 'None'),
        ('h', 'Human'),
        ('a', 'Autonomous'),
        ('b', 'Both'),
    )
    unique_scout_key = models.CharField(max_length=64, blank=True, null=True)
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    snow_days = models.IntegerField(default=0)
    starts_on_hab_2 = models.BooleanField(default=False)
    cargo_in_sandstorm = models.IntegerField(default=0)
    hatches_in_sandstorm = models.IntegerField(default=0)
    cargo_in_teleop = models.IntegerField(default=0)
    hatches_in_teleop = models.IntegerField(default=0)
    climb_level = models.IntegerField(default=0)
    max_rocket_height = models.IntegerField(default=1)
    ground_pickup_cargo = models.BooleanField(default=False)
    ground_pickup_hatch = models.BooleanField(default=False)
    favorite_feature = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=0)
    do_not_pick = models.BooleanField(default=False)
    scouter = models.CharField(max_length=255, blank=True, null=True)
    buddy_climb = models.BooleanField(default=False)

    @property
    def pit_scout_pk(self):
        return f'pit_{self.id}'


class MatchScout(models.Model):
    ALLIANCE_CHOICES = (
        ('b', 'Blue'),
        ('r', 'Red')
    )

    START_POSITION_CHOICES = (
        ('1', 'Hab Level 1'),
        ('2', 'Hab Level 2'),
    )

    LEVEL_CHOICES = (
        ('0', 'None'),
        ('1', 'Hab Level 1'),
        ('2', 'Hab Level 2'),
        ('3', 'Hab Level 3'),
    )

    unique_scout_key = models.CharField(max_length=64, blank=True, null=True)
    scouter = models.CharField(max_length=45)
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    alliance = models.CharField(max_length=1, default='b')
    match_number = models.IntegerField()
    event_date = models.DateTimeField(auto_now=True)
    start_position = models.CharField(max_length=1, choices=START_POSITION_CHOICES, default='1')
    hab_level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default='0')
    hab_level_int = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    strategy = models.IntegerField(default=0)
    team_work = models.IntegerField(default=0)
    recommend = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    in_match_actions = models.TextField(blank=True, null=True)
    hatch_count = models.IntegerField(default=0)
    cargo_count = models.IntegerField(default=0)

    def __str__(self):
        return 'robot number: ' + str(self.robot) + ' | match number: ' + str(self.match_number)

    class Meta:
        ordering = ['match_number']

    @property
    def match_pk(self):
        return f'match_{self.id}'


class CoachScout(models.Model):
    unique_scout_key = models.CharField(max_length=64, blank=True, null=True)
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    match_number = models.IntegerField(default=0)
    synergy = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)
    scouter = models.CharField(max_length=255, blank=True, null=True)
