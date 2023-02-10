from django.apps import AppConfig


class DanceschoolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'danceschool'

    def ready(self):
        import danceschool.signals
