from django.contrib import admin
from django.apps import apps

apps = apps.get_app_config('api')
admin.site.register(apps.get_models())
