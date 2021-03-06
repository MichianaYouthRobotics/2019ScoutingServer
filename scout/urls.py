from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'scout'

urlpatterns = [
    path('all-robots/<int:event>/', views.RobotList.as_view()),
    path('best-robots/hatches/', views.TopHatchRobotList.as_view()),
    path('best-robots/cargo/', views.TopCargoRobotList.as_view()),
    path('best-robots/climb/', views.TopClimbRobotList.as_view()),
    path('pit/list/<int:event>/', views.PitScouts.as_view()),
    path('pit/sync/<int:event_id>/', views.sync_pit_scouts),
    path('match/list/<int:event>/', views.MatchScouts.as_view()),
    path('match/sync/<int:event_id>/', views.sync_match_scouts),
    path('coach/list/<int:event>/', views.CoachScouts.as_view()),
    path('coach/sync/<int:event_id>/', views.sync_coach_scouts),
    path('event/<int:pk>/', views.event_login),
    path('fix-hab-levels/', views.fix_hab_levels),
    path('pdf/hatches/<int:event_id>/', views.print_hatches),
    path('pdf/cargo/<int:event_id>/', views.print_cargo),
    path('pdf/climb/<int:event_id>/', views.print_climb)

]

urlpatterns = format_suffix_patterns(urlpatterns)
