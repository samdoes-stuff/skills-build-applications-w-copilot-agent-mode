from rest_framework.routers import DefaultRouter
from .views import LeaderboardEntryViewSet

router = DefaultRouter()
router.register(r'leaderboard', LeaderboardEntryViewSet)

urlpatterns = router.urls
