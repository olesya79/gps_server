from django_filters import rest_framework as filters
from point.models import Point


class PointFilter(filters.FilterSet):
    name = filters.CharFilter()
    alias = filters.CharFilter()

    class Meta:
        model = Point
        fields = ['name', 'alias']
