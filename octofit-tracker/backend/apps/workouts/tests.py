from django.test import TestCase
from .models import Workout

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user_id='user1', activity='Running', duration=30)
        self.assertEqual(workout.activity, 'Running')
