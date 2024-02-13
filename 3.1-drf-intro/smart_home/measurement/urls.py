from django.urls import path
from measurement.views import SensorListView

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
]
