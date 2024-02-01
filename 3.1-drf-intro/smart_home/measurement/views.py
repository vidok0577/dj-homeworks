# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor
from measurement.serializers import SensorSerializer


class SensorListView(APIView):
    def get(self,request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)


class SensorView(APIView):
    pass
