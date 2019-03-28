from django.contrib import admin
from django.db import models

from .models import Event, Robot, MatchScout, CoachScout, PitScout

from django.forms import CheckboxSelectMultiple

class EventAdmin(admin.ModelAdmin):
    formfield_overrides = {
        Event.robots: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Event, EventAdmin)
admin.site.register(Robot)
admin.site.register(MatchScout)
admin.site.register(CoachScout)
admin.site.register(PitScout)

