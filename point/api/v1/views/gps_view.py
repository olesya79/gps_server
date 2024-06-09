from point.models import GPS
from core.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from point.api.v1.serializers.gps_serializer import GPSSerializer


class APIListPaginationGPS(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 10


class GPSViewSet(viewsets.ModelViewSet):
    queryset = GPS.objects.all()
    serializer_class = GPSSerializer
    pagination_class = APIListPaginationGPS
    permission_classes = (IsAuthenticated,)


