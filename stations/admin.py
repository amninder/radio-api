from django.contrib import admin
from stations.models import Station

class StationAdmin(admin.ModelAdmin):
	list_display		= ('name', 'school', 'state', 'lat', 'lng', 'url')

admin.site.register(Station, StationAdmin)