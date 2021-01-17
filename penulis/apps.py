from django.apps import AppConfig


class PenulisConfig(AppConfig):
    name = 'penulis'

    def ready(self):
        import penulis.signals

