from django.contrib import admin
from .models import QRCode


@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'target_url', 'is_active', 'scan_count', 'created_at')
    search_fields = ('code',)
    list_filter = ('is_active',)
