from django.contrib import admin
from .models import ExpertModel
# Register your models here.

class ExpertAdmin(admin.ModelAdmin):
    list_display = ('name','rating',)

admin.site.register(ExpertModel,ExpertAdmin)