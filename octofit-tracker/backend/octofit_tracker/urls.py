from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': request.build_absolute_uri('users/'),
        'activities': request.build_absolute_uri('activities/'),
        'teams': request.build_absolute_uri('teams/'),
        'leaderboard': request.build_absolute_uri('leaderboard/'),
        'workouts': request.build_absolute_uri('workouts/'),
    })

urlpatterns = [
    path('', api_root, name='api_root'),
    path('users/', include('apps.users.urls')),
    path('activities/', include('apps.activities.urls')),
    path('teams/', include('apps.teams.urls')),
    path('leaderboard/', include('apps.leaderboard.urls')),
    path('workouts/', include('apps.workouts.urls')),
]