from rest_framework.routers import DefaultRouter
from .views import WorkoutViewSet

router = DefaultRouter()
router.register(r'', WorkoutViewSet)

urlpatterns = router.urls
