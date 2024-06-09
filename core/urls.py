from point.api.v1.views.gps_view import GPSViewSet
from point.api.v1.views.point_view import PointViewSet

from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'gps', GPSViewSet)
router.register(r'point', PointViewSet)

urlpatterns = router.urls