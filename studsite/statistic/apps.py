from django.apps import AppConfig


class StatisticConfig(AppConfig):
    name = 'statistic'

    def ready(self):
        from . import signals
