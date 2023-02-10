from django.apps import AppConfig


class BooktrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booktracker'
    verbose_name = 'Читательский прогресс'

    def ready(self):
        import booktracker.signals