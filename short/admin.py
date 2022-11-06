from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    class Meta:
        model = Link
    fields = ['initial_url','new_url', 'user']
    list_display = ['id', 'initial_url','new_url', 'user', 'time_created',]



admin.site.register(Link, LinkAdmin)


