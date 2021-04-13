from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'acme_bank_api.users'
    verbose_name = "Users"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        try:
            import acme_bank_api.users.signals  # noqa F401
        except ImportError:
            pass
