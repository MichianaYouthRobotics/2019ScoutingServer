from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'scout'

urlpatterns = [
    path('all-robots/<int:event>/', views.RobotList.as_view()),
    # path('all-matches/', views.MatchList.as_view()),
    path('pit/list/<int:event>/', views.PitScouts.as_view()),
    path('match/list/<int:event>/', views.MatchScouts.as_view()),
    path('coach/list/<int:event>/', views.CoachScouts.as_view()),

    path('event/<int:pk>/', views.event_login),

]

urlpatterns = format_suffix_patterns(urlpatterns)
