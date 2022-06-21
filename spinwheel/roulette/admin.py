from django.contrib import admin
from roulette import models


@admin.register(models.Round)
class RoundAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_deleted']


@admin.register(models.Spin)
class SpinAdmin(admin.ModelAdmin):
    list_display = ['id', 'spin_round_id', 'user_id', 'value']
