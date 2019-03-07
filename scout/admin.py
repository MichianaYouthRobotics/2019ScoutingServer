from django.contrib import admin

from .models import Event, Robot, MatchScout, CoachScout, PitScout

admin.site.register(Event)
admin.site.register(Robot)
admin.site.register(MatchScout)
admin.site.register(CoachScout)
admin.site.register(PitScout)

