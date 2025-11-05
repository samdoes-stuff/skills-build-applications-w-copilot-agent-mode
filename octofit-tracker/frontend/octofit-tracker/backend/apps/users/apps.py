try:
    from django.apps import AppConfig  # type: ignore
except Exception:
    # Fallback stub for environments where Django is not available to
    # avoid "could not be resolved from source" errors in editors/linters.
    class AppConfig:
        """Minimal fallback AppConfig stub used only when Django is unavailable."""
        pass

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
