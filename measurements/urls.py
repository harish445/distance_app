from django.urls import URLPattern, path
from .views import calculate_distance_view

app_name = 'measurements'

urlpatterns = [
    path('', calculate_distance_view, name='calculate-view'),
]