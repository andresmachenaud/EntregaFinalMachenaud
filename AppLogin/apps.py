from django.apps import AppConfig


class ApploginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppLogin'

    def ready(self):
        import AppLogin.signals