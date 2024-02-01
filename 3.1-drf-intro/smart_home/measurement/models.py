from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=150, verbose_name='Описание')


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField()
    created_at = models.DateTimeField(auto_now_add=True)
