from django.apps import AppConfig


class MyCollectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_collection'
    verbose_name = 'Моя коллекция'
