from django.contrib import admin
from .models import Felmeres, Iranyitoszam

class IranyitoszamAdmin(admin.ModelAdmin):
    list_display=('varos', 'irSzam',)
    search_fields=['varos']
    
admin.site.register(Felmeres)
admin.site.register(Iranyitoszam, IranyitoszamAdmin)
