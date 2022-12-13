from django.contrib import admin
from .models import Sites

class SitesAdmin(admin.ModelAdmin):
  
    list_display = ('domain_name','display_name')


admin.site.register(Sites,SitesAdmin)
