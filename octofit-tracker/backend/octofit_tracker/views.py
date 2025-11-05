from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bson import ObjectId
from datetime import datetime
from .models import (
    get_users_collection, get_teams_collection, get_activities_collection,
    get_leaderboard_collection, get_workouts_collection
)
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)

@api_view(['GET', 'POST'])
def users_list(request):
    """List all users or create a new user"""
    collection = get_users_collection()
    
    if request.method == 'GET':
        users = list(collection.find())
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            user_data['created_at'] = datetime.utcnow()
            result = collection.insert_one(user_data)
            user_data['_id'] = result.inserted_id
            return Response(UserSerializer(user_data).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """Retrieve, update or delete a user"""
    collection = get_users_collection()
    
    try:
        user = collection.find_one({'_id': ObjectId(pk)})
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            collection.update_one({'_id': ObjectId(pk)}, {'$set': serializer.validated_data})
            user = collection.find_one({'_id': ObjectId(pk)})
            return Response(UserSerializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        collection.delete_one({'_id': ObjectId(pk)})
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def teams_list(request):
    """List all teams or create a new team"""
    collection = get_teams_collection()
    
    if request.method == 'GET':
        teams = list(collection.find())
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            team_data = serializer.validated_data
            team_data['created_at'] = datetime.utcnow()
            result = collection.insert_one(team_data)
            team_data['_id'] = result.inserted_id
            return Response(TeamSerializer(team_data).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, pk):
    """Retrieve, update or delete a team"""
    collection = get_teams_collection()
    
    try:
        team = collection.find_one({'_id': ObjectId(pk)})
        if not team:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            collection.update_one({'_id': ObjectId(pk)}, {'$set': serializer.validated_data})
            team = collection.find_one({'_id': ObjectId(pk)})
            return Response(TeamSerializer(team).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        collection.delete_one({'_id': ObjectId(pk)})
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def activities_list(request):
    """List all activities or create a new activity"""
    collection = get_activities_collection()
    
    if request.method == 'GET':
        activities = list(collection.find())
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            activity_data = serializer.validated_data
            activity_data['created_at'] = datetime.utcnow()
            result = collection.insert_one(activity_data)
            activity_data['_id'] = result.inserted_id
            return Response(ActivitySerializer(activity_data).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def activity_detail(request, pk):
    """Retrieve, update or delete an activity"""
    collection = get_activities_collection()
    
    try:
        activity = collection.find_one({'_id': ObjectId(pk)})
        if not activity:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            collection.update_one({'_id': ObjectId(pk)}, {'$set': serializer.validated_data})
            activity = collection.find_one({'_id': ObjectId(pk)})
            return Response(ActivitySerializer(activity).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        collection.delete_one({'_id': ObjectId(pk)})
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def leaderboard_list(request):
    """List all leaderboard entries or create a new entry"""
    collection = get_leaderboard_collection()
    
    if request.method == 'GET':
        leaderboard = list(collection.find().sort('rank', 1))
        serializer = LeaderboardSerializer(leaderboard, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = LeaderboardSerializer(data=request.data)
        if serializer.is_valid():
            leaderboard_data = serializer.validated_data
            leaderboard_data['updated_at'] = datetime.utcnow()
            result = collection.insert_one(leaderboard_data)
            leaderboard_data['_id'] = result.inserted_id
            return Response(LeaderboardSerializer(leaderboard_data).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def leaderboard_detail(request, pk):
    """Retrieve, update or delete a leaderboard entry"""
    collection = get_leaderboard_collection()
    
    try:
        leaderboard = collection.find_one({'_id': ObjectId(pk)})
        if not leaderboard:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = LeaderboardSerializer(leaderboard)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = LeaderboardSerializer(data=request.data)
        if serializer.is_valid():
            leaderboard_data = serializer.validated_data
            leaderboard_data['updated_at'] = datetime.utcnow()
            collection.update_one({'_id': ObjectId(pk)}, {'$set': leaderboard_data})
            leaderboard = collection.find_one({'_id': ObjectId(pk)})
            return Response(LeaderboardSerializer(leaderboard).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        collection.delete_one({'_id': ObjectId(pk)})
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def workouts_list(request):
    """List all workouts or create a new workout"""
    collection = get_workouts_collection()
    
    if request.method == 'GET':
        workouts = list(collection.find())
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            workout_data = serializer.validated_data
            workout_data['created_at'] = datetime.utcnow()
            result = collection.insert_one(workout_data)
            workout_data['_id'] = result.inserted_id
            return Response(WorkoutSerializer(workout_data).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def workout_detail(request, pk):
    """Retrieve, update or delete a workout"""
    collection = get_workouts_collection()
    
    try:
        workout = collection.find_one({'_id': ObjectId(pk)})
        if not workout:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            collection.update_one({'_id': ObjectId(pk)}, {'$set': serializer.validated_data})
            workout = collection.find_one({'_id': ObjectId(pk)})
            return Response(WorkoutSerializer(workout).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        collection.delete_one({'_id': ObjectId(pk)})
        return Response(status=status.HTTP_204_NO_CONTENT)
