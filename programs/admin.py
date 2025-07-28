from django.contrib import admin
from .models import ProgramModel

# Register your models here.


class ProgramModelAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'description',)


admin.site.register(ProgramModel, ProgramModelAdmin)