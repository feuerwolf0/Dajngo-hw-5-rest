from django.urls import path

from .views import SensorView, SensorUpdateView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorView.as_view(), name='sensors'),
    path('sensors/<int:pk>/', SensorUpdateView.as_view(), name='update_sensor'),
    path('measurements/', MeasurementCreateView.as_view(), name='create_measurement')
]
