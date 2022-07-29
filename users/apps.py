from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

        # Implicitly connect signal handlers decorated with @receiver.
    def ready(self):
        import users.signals
