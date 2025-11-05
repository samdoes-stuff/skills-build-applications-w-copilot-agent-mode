from rest_framework import viewsets
from .models import LeaderboardEntry
from .serializers import LeaderboardEntrySerializer

class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all()
    serializer_class = LeaderboardEntrySerializer
