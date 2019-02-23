from django.contrib import admin

from .models import Event, Robot, Match, CoachScout, PitScout, EndGame, InGame

admin.site.register(Event)
admin.site.register(Robot)
admin.site.register(Match)
admin.site.register(CoachScout)
admin.site.register(PitScout)
admin.site.register(EndGame)
admin.site.register(InGame)

