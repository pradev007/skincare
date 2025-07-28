from django.contrib import admin
from .models import Services

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('treatments', 'duration', 'price', 'is_popular')
admin.site.register(Services, ServiceAdmin)