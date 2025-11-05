from django.conf import settings
from pymongo import MongoClient

# MongoDB connection
def get_db():
    client = MongoClient(
        host=settings.MONGODB_SETTINGS['host'],
        port=settings.MONGODB_SETTINGS['port']
    )
    return client[settings.MONGODB_SETTINGS['db']]

# Collection helpers
def get_users_collection():
    db = get_db()
    return db['users']

def get_teams_collection():
    db = get_db()
    return db['teams']

def get_activities_collection():
    db = get_db()
    return db['activities']

def get_leaderboard_collection():
    db = get_db()
    return db['leaderboard']

def get_workouts_collection():
    db = get_db()
    return db['workouts']
