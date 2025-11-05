import os
import sys
import glob
import random
from datetime import datetime, timedelta

# Try to add the project's virtualenv site-packages to sys.path so editors/linters can resolve Django.
# This looks for octofit-tracker/backend/venv/lib/python*/site-packages relative to this file.
# Prefer the venv inside the backend directory, but also fall back to a parent venv if present.
venv_dirs = [
    os.path.join(os.path.dirname(__file__), 'venv', 'lib', 'python*', 'site-packages'),
    os.path.join(os.path.dirname(__file__), '..', 'venv', 'lib', 'python*', 'site-packages'),
]
venv_site_packages = []
for pattern in venv_dirs:
    venv_site_packages.extend(glob.glob(pattern))
# de-duplicate while preserving order
venv_site_packages = list(dict.fromkeys(venv_site_packages))
for path in venv_site_packages:
    abs_path = os.path.abspath(path)
    if abs_path not in sys.path:
        sys.path.insert(0, abs_path)

try:
    import django  # type: ignore
except ImportError:
    raise ImportError(
        "Django could not be imported. Create and activate the project's virtual environment and install requirements:\n"
        "python3 -m venv octofit-tracker/backend/venv\n"
        "source octofit-tracker/backend/venv/bin/activate\n"
        "pip install -r octofit-tracker/backend/requirements.txt\n"
        "After that, rerun this script."
    )

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from apps.users.models import User
from apps.activities.models import Activity
from apps.teams.models import Team
from apps.leaderboard.models import LeaderboardEntry
from apps.workouts.models import Workout

# Create test users
def create_users():
    users = []
    for i in range(5):
        user, _ = User.objects.get_or_create(username=f'user{i}', email=f'user{i}@example.com')
        users.append(user)
    return users

# Create test activities
def create_activities(users):
    for user in users:
        for i in range(3):
            Activity.objects.get_or_create(
                name=f'Activity {i}',
                user=user,
                date=datetime.now() - timedelta(days=random.randint(0, 10))
            )

# Create test teams
def create_teams(users):
    for i in range(2):
        team, _ = Team.objects.get_or_create(name=f'Team {i}')
        team.members = [user.username for user in users[i*2:(i+1)*2]]
        team.save()

# Create test leaderboard entries
def create_leaderboard(users):
    for user in users:
        LeaderboardEntry.objects.get_or_create(user_id=user.username, score=random.randint(0, 100))

# Create test workouts
def create_workouts(users):
    for user in users:
        for i in range(2):
            Workout.objects.get_or_create(
                user_id=user.username,
                activity=f'Workout {i}',
                duration=random.randint(20, 60),
                date=datetime.now() - timedelta(days=random.randint(0, 10))
            )

def main():
    users = create_users()
    create_activities(users)
    create_teams(users)
    create_leaderboard(users)
    create_workouts(users)
    print('Test data created.')

if __name__ == '__main__':
    main()
