from rest_framework import serializers
from bson import ObjectId

class ObjectIdField(serializers.Field):
    """Custom field to handle MongoDB ObjectId"""
    def to_representation(self, value):
        return str(value)
    
    def to_internal_value(self, data):
        try:
            return ObjectId(data)
        except:
            raise serializers.ValidationError("Invalid ObjectId")

class UserSerializer(serializers.Serializer):
    _id = ObjectIdField(read_only=True)
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    team_id = ObjectIdField(required=False, allow_null=True)
    total_points = serializers.IntegerField(default=0)
    created_at = serializers.DateTimeField(read_only=True)

class TeamSerializer(serializers.Serializer):
    _id = ObjectIdField(read_only=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False, allow_blank=True)
    members = serializers.ListField(child=ObjectIdField(), default=list)
    total_points = serializers.IntegerField(default=0)
    created_at = serializers.DateTimeField(read_only=True)

class ActivitySerializer(serializers.Serializer):
    _id = ObjectIdField(read_only=True)
    user_id = ObjectIdField()
    activity_type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()  # in minutes
    distance = serializers.FloatField(required=False, allow_null=True)  # in miles
    points = serializers.IntegerField()
    date = serializers.DateTimeField()
    created_at = serializers.DateTimeField(read_only=True)

class LeaderboardSerializer(serializers.Serializer):
    _id = ObjectIdField(read_only=True)
    entity_type = serializers.CharField(max_length=50)  # 'user' or 'team'
    entity_id = ObjectIdField()
    entity_name = serializers.CharField(max_length=200)
    total_points = serializers.IntegerField()
    rank = serializers.IntegerField()
    updated_at = serializers.DateTimeField(read_only=True)

class WorkoutSerializer(serializers.Serializer):
    _id = ObjectIdField(read_only=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField()
    activity_type = serializers.CharField(max_length=100)
    difficulty = serializers.CharField(max_length=50)
    duration = serializers.IntegerField()  # in minutes
    points = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
