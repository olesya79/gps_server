from rest_framework import serializers

from point.models import Point


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ['name']
