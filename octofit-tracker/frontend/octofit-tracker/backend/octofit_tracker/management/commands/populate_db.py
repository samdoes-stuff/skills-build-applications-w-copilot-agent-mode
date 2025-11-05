"""
Populate the octofit_db database with test data
"""
from django.core.management.base import BaseCommand
from apps.users.models import User
from apps.activities.models import Activity
from apps.teams.models import Team
from apps.leaderboard.models import LeaderboardEntry
from apps.workouts.models import Workout
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        users = self.create_users()
        self.create_activities(users)
        self.create_teams(users)
        self.create_leaderboard(users)
        self.create_workouts(users)
        self.stdout.write(self.style.SUCCESS('Test data created.'))

    def create_users(self):
        users = []
        for i in range(5):
            user, created = User.objects.get_or_create(
                username=f'user{i}',
                defaults={"email": f'user{i}@example.com'}
            )
            if created:
                user.set_password('testpassword')
                user.save()
                user.refresh_from_db()
            else:
                if not user.has_usable_password():
                    user.set_password('testpassword')
                    user.save()
            users.append(user)
        self.stdout.write('User list after creation:')
        for user in users:
            self.stdout.write(f"User: pk={user.pk}, username={user.username}, email={user.email}")
        return users

    def create_activities(self, users):
        for user in users:
            user = User.objects.get(pk=user.pk)
            for i in range(3):
                Activity.objects.get_or_create(
                    user=user,
                    activity_type=f'Activity {i}',
                    defaults={
                        'duration': timedelta(minutes=random.randint(20, 60)),
                        'distance': round(random.uniform(1.0, 10.0), 2),
                        'date': datetime.now() - timedelta(days=random.randint(0, 10))
                    }
                )

    def create_teams(self, users):
        Team.objects.all().delete()
        for i in range(2):
            team, _ = Team.objects.get_or_create(name=f'Team {i}')
            team.members = [user.username for user in users[i*2:(i+1)*2]]
            team.save()

    def create_leaderboard(self, users):
        for user in users:
            LeaderboardEntry.objects.get_or_create(user_id=str(user.pk), defaults={"score": random.randint(0, 100)})

    def create_workouts(self, users):
        for user in users:
            for i in range(2):
                Workout.objects.get_or_create(
                    user_id=str(user.pk),
                    activity=f'Workout {i}',
                    defaults={
                        "duration": random.randint(20, 60),
                        "date": datetime.now() - timedelta(days=random.randint(0, 10))
                    }
                )
