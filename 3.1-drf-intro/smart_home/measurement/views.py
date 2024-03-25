# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import GenericAPIView, CreateAPIView, ListCreateAPIView, ListAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer


class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdateRetrieveView(GenericAPIView, UpdateModelMixin, RetrieveModelMixin):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def get(self, request, *args, **kwargs):
        result = self.retrieve(request, *args, **kwargs).data
        measurements = Measurement.objects.filter(sensor=kwargs['pk'])
        ser = MeasurementSerializer(measurements, many=True)
        result['measumremnts'] = ser.data
        print(ser.data)
        print(measurements)
        return Response(data=result)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class MeasurementSensorsListView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.get(request, *args, **kwargs)
