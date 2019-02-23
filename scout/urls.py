from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'scout'

urlpatterns = [
    path('robot/list/', views.RobotList.as_view()),
    path('match/list/', views.MatchList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
