from django.contrib import admin
from . models import Audio
# Register your models here.

class AudioAdmin(admin.ModelAdmin):
    list_display = ("id","audio_file","text")
    search_fields = ("text",)

admin.site.register(Audio,AudioAdmin)