from django.contrib import admin
from goonsay.apps.goonsay.models import GoonSay

class GoonSayAdmin(admin.ModelAdmin):
    pass

admin.site.register(GoonSay, GoonSayAdmin)
