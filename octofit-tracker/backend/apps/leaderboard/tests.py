from django.test import TestCase
from .models import LeaderboardEntry

class LeaderboardEntryModelTest(TestCase):
    def test_create_entry(self):
        entry = LeaderboardEntry.objects.create(user_id='user1', score=100)
        self.assertEqual(entry.score, 100)
