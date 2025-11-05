from django.urls import path, include

import os
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request, format=None):
    # Get Codespace name from environment variable
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        # fallback to request host (localhost or other)
        base_url = request.build_absolute_uri('/')
        if not base_url.endswith('/'):
            base_url += '/'
        base_url += 'api/' if not base_url.endswith('api/') else ''
    return Response({
        'users': f"{base_url}users/",
        'activities': f"{base_url}activities/",
        'teams': f"{base_url}teams/",
        'leaderboard': f"{base_url}leaderboard/",
        'workouts': f"{base_url}workouts/",
    })

urlpatterns = [
    path('', api_root, name='api_root'),
    path('users/', include('apps.users.urls')),
    path('activities/', include('apps.activities.urls')),
    path('teams/', include('apps.teams.urls')),
    path('leaderboard/', include('apps.leaderboard.urls')),
    path('workouts/', include('apps.workouts.urls')),
]