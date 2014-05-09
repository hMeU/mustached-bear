from django.contrib import admin
from basics.models import IP

class IPAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['addr', 'os', 'browser'] }),
    ]
    list_display = ('addr', 'os', 'browser')

admin.site.register(IP, IPAdmin)
