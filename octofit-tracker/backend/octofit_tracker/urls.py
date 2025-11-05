"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from . import views
import os

@api_view(['GET'])
def api_root(request, format=None):
    """API root endpoint"""
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        base_url = "http://localhost:8000"
    
    return Response({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activities': f'{base_url}/api/activities/',
        'leaderboard': f'{base_url}/api/leaderboard/',
        'workouts': f'{base_url}/api/workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api/', api_root, name='api-root'),
    path('api/users/', views.users_list, name='users-list'),
    path('api/users/<str:pk>/', views.user_detail, name='user-detail'),
    path('api/teams/', views.teams_list, name='teams-list'),
    path('api/teams/<str:pk>/', views.team_detail, name='team-detail'),
    path('api/activities/', views.activities_list, name='activities-list'),
    path('api/activities/<str:pk>/', views.activity_detail, name='activity-detail'),
    path('api/leaderboard/', views.leaderboard_list, name='leaderboard-list'),
    path('api/leaderboard/<str:pk>/', views.leaderboard_detail, name='leaderboard-detail'),
    path('api/workouts/', views.workouts_list, name='workouts-list'),
    path('api/workouts/<str:pk>/', views.workout_detail, name='workout-detail'),
]
