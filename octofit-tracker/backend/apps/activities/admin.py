try:
    from django.contrib import admin  # type: ignore
except ImportError:
    # Fallback stub for environments where Django isn't installed (e.g., static analysis)
    class _DummyAdminModule:
        class ModelAdmin:
            pass

        def register(self, model):
            def decorator(cls):
                return cls
            return decorator

    admin = _DummyAdminModule()

from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'date')
