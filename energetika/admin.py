from django.contrib import admin
from .models import Megrendeles, Iranyitoszam

class IranyitoszamAdmin(admin.ModelAdmin):
    list_display=('varos', 'irSzam',)
    search_fields=['varos']
    
admin.site.register(Megrendeles)
admin.site.register(Iranyitoszam, IranyitoszamAdmin)
