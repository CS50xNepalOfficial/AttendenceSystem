from django.contrib import admin
from .models import Event, ScannedQR

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')

@admin.register(ScannedQR)
class ScannedQRAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'is_scanned')
