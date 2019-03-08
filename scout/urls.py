from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'scout'

urlpatterns = [
    path('all-robots/<int:event>/', views.RobotList.as_view()),
    path('pit/list/<int:event>/', views.PitScouts.as_view()),
    path('pit/sync/<int:event_id>/', views.sync_pit_scouts),
    path('match/list/<int:event>/', views.MatchScouts.as_view()),
    path('match/sync/<int:event_id>/', views.sync_match_scouts),
    path('coach/list/<int:event>/', views.CoachScouts.as_view()),
    path('coach/sync/<int:event_id>/', views.sync_coach_scouts),
    path('event/<int:pk>/', views.event_login),

]

urlpatterns = format_suffix_patterns(urlpatterns)
