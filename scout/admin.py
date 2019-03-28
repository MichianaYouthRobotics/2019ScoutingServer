from django.contrib import admin

from .models import Event, Robot, MatchScout, CoachScout, PitScout

from django.forms import CheckboxSelectMultiple

class EventAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'robots': CheckboxSelectMultiple},
    }

admin.site.register(Event, EventAdmin)
admin.site.register(Robot)
admin.site.register(MatchScout)
admin.site.register(CoachScout)
admin.site.register(PitScout)

