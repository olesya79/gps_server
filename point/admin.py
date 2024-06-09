from point.models import Point
from point.models import GPS
from django.contrib import admin


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['point_id', 'name', 'alias']
    ordering = ['name']
    search_fields = ['name__isstartwith']


@admin.register(GPS)
class GPSAdmin(admin.ModelAdmin):
    list_display = ['gps_id', 'point_gps_id', 'lat', 'lon', 'speed', 'time', 'point_id']
    ordering = ['time']
    search_fields = ['time__isstartwith']


# Register your models here.
