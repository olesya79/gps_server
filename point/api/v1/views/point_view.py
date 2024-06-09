from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from core.permissions import IsAuthenticated
from core.filters.point_filters import PointFilter

from point.api.v1.serializers.point_serializer import PointSerializer
from point.api.v1.views.gps_view import APIListPaginationGPS
from point.models import Point


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    pagination_class = APIListPaginationGPS
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = PointFilter
