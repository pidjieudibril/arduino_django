# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... Autres URL ...
    path('save_sensor_data/', views.save_sensor_data, name='save_sensor_data'),
    path('afficheTemperature', views.afficheTemperature, name='afficheTemperature'), 
    path('afficheTemperature1', views.afficheTemperature1, name='afficheTemperature1'), 
]
