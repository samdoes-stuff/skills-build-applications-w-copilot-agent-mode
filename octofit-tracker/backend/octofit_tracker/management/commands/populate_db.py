from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from bson import ObjectId
from octofit_tracker.models import (
    get_users_collection, get_teams_collection, get_activities_collection,
    get_leaderboard_collection, get_workouts_collection, get_db
)

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Populating database with test data...')
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        users_collection = get_users_collection()
        teams_collection = get_teams_collection()
        activities_collection = get_activities_collection()
        leaderboard_collection = get_leaderboard_collection()
        workouts_collection = get_workouts_collection()
        
        users_collection.delete_many({})
        teams_collection.delete_many({})
        activities_collection.delete_many({})
        leaderboard_collection.delete_many({})
        workouts_collection.delete_many({})
        
        # Create unique index on email for users
        db = get_db()
        db.users.create_index([("email", 1)], unique=True)
        
        # Create teams
        self.stdout.write('Creating teams...')
        team_marvel = {
            'name': 'Team Marvel',
            'description': 'Earth\'s Mightiest Heroes fitness team',
            'members': [],
            'total_points': 0,
            'created_at': datetime.utcnow()
        }
        team_dc = {
            'name': 'Team DC',
            'description': 'Justice League fitness warriors',
            'members': [],
            'total_points': 0,
            'created_at': datetime.utcnow()
        }
        
        marvel_result = teams_collection.insert_one(team_marvel)
        dc_result = teams_collection.insert_one(team_dc)
        marvel_id = marvel_result.inserted_id
        dc_id = dc_result.inserted_id
        
        # Create users (Marvel heroes)
        self.stdout.write('Creating Marvel heroes...')
        marvel_users = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'team_id': marvel_id, 'total_points': 450},
            {'name': 'Steve Rogers', 'email': 'captainamerica@marvel.com', 'team_id': marvel_id, 'total_points': 520},
            {'name': 'Thor Odinson', 'email': 'thor@marvel.com', 'team_id': marvel_id, 'total_points': 480},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com', 'team_id': marvel_id, 'total_points': 390},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com', 'team_id': marvel_id, 'total_points': 510},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com', 'team_id': marvel_id, 'total_points': 470},
        ]
        
        # Create users (DC heroes)
        self.stdout.write('Creating DC heroes...')
        dc_users = [
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'team_id': dc_id, 'total_points': 540},
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'team_id': dc_id, 'total_points': 580},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'team_id': dc_id, 'total_points': 560},
            {'name': 'Barry Allen', 'email': 'flash@dc.com', 'team_id': dc_id, 'total_points': 490},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com', 'team_id': dc_id, 'total_points': 440},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com', 'team_id': dc_id, 'total_points': 460},
        ]
        
        all_users = marvel_users + dc_users
        for user_data in all_users:
            user_data['created_at'] = datetime.utcnow()
        
        users_result = users_collection.insert_many(all_users)
        user_ids = users_result.inserted_ids
        
        # Update team members
        marvel_user_ids = user_ids[:6]
        dc_user_ids = user_ids[6:]
        
        teams_collection.update_one(
            {'_id': marvel_id},
            {'$set': {'members': marvel_user_ids, 'total_points': sum(u['total_points'] for u in marvel_users)}}
        )
        teams_collection.update_one(
            {'_id': dc_id},
            {'$set': {'members': dc_user_ids, 'total_points': sum(u['total_points'] for u in dc_users)}}
        )
        
        # Create activities
        self.stdout.write('Creating activities...')
        activities = []
        activity_types = ['Running', 'Cycling', 'Swimming', 'Strength Training', 'Yoga']
        
        for i, user_id in enumerate(user_ids):
            for j in range(3):  # 3 activities per user
                activity = {
                    'user_id': user_id,
                    'activity_type': activity_types[(i + j) % len(activity_types)],
                    'duration': 30 + (i * 5) + (j * 10),
                    'distance': 3.0 + (i * 0.5) if activity_types[(i + j) % len(activity_types)] in ['Running', 'Cycling'] else None,
                    'points': 50 + (i * 5) + (j * 10),
                    'date': datetime.utcnow() - timedelta(days=j),
                    'created_at': datetime.utcnow()
                }
                activities.append(activity)
        
        activities_collection.insert_many(activities)
        
        # Create leaderboard entries
        self.stdout.write('Creating leaderboard...')
        leaderboard_entries = []
        
        # User leaderboard
        all_users_sorted = sorted(all_users, key=lambda x: x['total_points'], reverse=True)
        for rank, user_data in enumerate(all_users_sorted, 1):
            user_id = users_collection.find_one({'email': user_data['email']})['_id']
            entry = {
                'entity_type': 'user',
                'entity_id': user_id,
                'entity_name': user_data['name'],
                'total_points': user_data['total_points'],
                'rank': rank,
                'updated_at': datetime.utcnow()
            }
            leaderboard_entries.append(entry)
        
        # Team leaderboard
        teams_sorted = [
            {'name': 'Team DC', 'id': dc_id, 'points': sum(u['total_points'] for u in dc_users)},
            {'name': 'Team Marvel', 'id': marvel_id, 'points': sum(u['total_points'] for u in marvel_users)}
        ]
        
        for rank, team_data in enumerate(teams_sorted, 1):
            entry = {
                'entity_type': 'team',
                'entity_id': team_data['id'],
                'entity_name': team_data['name'],
                'total_points': team_data['points'],
                'rank': rank,
                'updated_at': datetime.utcnow()
            }
            leaderboard_entries.append(entry)
        
        leaderboard_collection.insert_many(leaderboard_entries)
        
        # Create workouts
        self.stdout.write('Creating workouts...')
        workouts = [
            {
                'name': 'Morning Cardio Blast',
                'description': 'High-intensity cardio workout to kickstart your day',
                'activity_type': 'Running',
                'difficulty': 'Hard',
                'duration': 45,
                'points': 150,
                'created_at': datetime.utcnow()
            },
            {
                'name': 'Strength Builder',
                'description': 'Full body strength training routine',
                'activity_type': 'Strength Training',
                'difficulty': 'Medium',
                'duration': 60,
                'points': 180,
                'created_at': datetime.utcnow()
            },
            {
                'name': 'Zen Flow Yoga',
                'description': 'Relaxing yoga session for flexibility and mindfulness',
                'activity_type': 'Yoga',
                'difficulty': 'Easy',
                'duration': 30,
                'points': 100,
                'created_at': datetime.utcnow()
            },
            {
                'name': 'Power Cycling',
                'description': 'Intense cycling workout for endurance',
                'activity_type': 'Cycling',
                'difficulty': 'Hard',
                'duration': 50,
                'points': 160,
                'created_at': datetime.utcnow()
            },
            {
                'name': 'Swimming Sprint',
                'description': 'Fast-paced swimming workout',
                'activity_type': 'Swimming',
                'difficulty': 'Medium',
                'duration': 40,
                'points': 140,
                'created_at': datetime.utcnow()
            }
        ]
        
        workouts_collection.insert_many(workouts)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with test data!'))
        self.stdout.write(f'Created {len(all_users)} users')
        self.stdout.write(f'Created 2 teams')
        self.stdout.write(f'Created {len(activities)} activities')
        self.stdout.write(f'Created {len(leaderboard_entries)} leaderboard entries')
        self.stdout.write(f'Created {len(workouts)} workouts')
