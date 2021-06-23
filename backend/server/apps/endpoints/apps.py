from django.apps import AppConfig


class EndpointsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #default_auto_field = 'django.db.models.AutoField'
    name = 'endpoints'
    default = False