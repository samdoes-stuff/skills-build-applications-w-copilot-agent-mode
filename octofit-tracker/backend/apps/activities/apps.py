from typing import TYPE_CHECKING
import importlib

if TYPE_CHECKING:
    # Allow type checkers to see AppConfig when Django is available.
    from django.apps import AppConfig  # type: ignore
else:
    try:
        django_apps = importlib.import_module('django.apps')
        AppConfig = getattr(django_apps, 'AppConfig')
    except Exception:
        # Fallback stub for environments where Django isn't available (e.g., editor/CI)
        class AppConfig:
            default_auto_field = None
            name = None

class ActivitiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.activities'
