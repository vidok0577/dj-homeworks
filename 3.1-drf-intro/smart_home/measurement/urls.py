from django.urls import path
from measurement.views import SensorListCreateView, SensorUpdateRetrieveView, MeasurementCreateView, \
    MeasurementSensorsListView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateRetrieveView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('measurement/', MeasurementSensorsListView.as_view())
]
