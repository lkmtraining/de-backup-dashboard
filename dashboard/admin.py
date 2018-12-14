from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Host, Backup

class HostAdmin(admin.ModelAdmin):
    pass

class BackupAdmin(admin.ModelAdmin):
    pass

admin.site.register(Host)
admin.site.register(Backup)
