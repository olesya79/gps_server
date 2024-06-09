from django.db import models

from core.abstract_models import Abstract


class Point(Abstract):
    """Represents object data"""
    point_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'

    def __str__(self):
        return self.name


class GPS(Abstract):
    """Represents location data."""
    gps_id = models.AutoField(primary_key=True)
    point_gps_id = models.IntegerField(blank=True)
    lat = models.FloatField(blank=True)
    lon = models.FloatField(blank=True)
    speed = models.FloatField(blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    point_id = models.ForeignKey(
        Point,
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ['point_gps_id']
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'

    def __str__(self):
        return self.point_gps_id

