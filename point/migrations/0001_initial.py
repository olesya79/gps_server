# Generated by Django 4.2.13 on 2024-06-09 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('point_id', models.IntegerField(blank=True)),
                ('name', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Имя',
                'verbose_name_plural': 'Имена',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_update', models.DateTimeField(auto_now=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('gps_id', models.IntegerField(blank=True)),
                ('point_gps_id', models.IntegerField(blank=True)),
                ('lat', models.FloatField(blank=True)),
                ('lon', models.FloatField(blank=True)),
                ('speed', models.FloatField(blank=True)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('point_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='point.point')),
            ],
            options={
                'verbose_name': 'Точка',
                'verbose_name_plural': 'Точки',
                'ordering': ['point_gps_id'],
            },
        ),
    ]
