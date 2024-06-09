from point.models import GPS
from rest_framework import serializers


class GPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPS
        fields = ['point_gps_id', 'lat', 'lon', 'speed', 'time']
