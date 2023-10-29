from django.http import JsonResponse
from .models import TemperatureData
from datetime import datetime
import serial  # bibliothèque pyserial
from django.shortcuts import render

def afficheTemperature(request, template_name='live_graph_.html'):
    latest_temperature_data = TemperatureData.objects.last()  # Obtenez la dernière entrée de la base de données
    return render(request, template_name, {'latest_temperature_data': latest_temperature_data})
def afficheTemperature1(request,template_name = 'live_graph.html'):
    return render(request, template_name)



def save_sensor_data(request):
    data = {}
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        COM4 = request.GET.get('id', None)
        sensor_val = 0.0  # Initialisation de la valeur du capteur
        now = datetime.now()
        ok_date = str(now.strftime('%Y-%m-%d %H:%M:%S'))

        try:
            sr = serial.Serial(COM4, 9600)
            st = list(str(sr.readline(), 'utf-8'))
            sr.close()
            sensor_val = float(''.join(st[:]))

            # Enregistrez la donnée dans la base de données
            temperature_data = TemperatureData(temperature=sensor_val, timestamp=now)
            temperature_data.save()
            data['result'] = "Données enregistrées avec succès."
        except Exception as e:
            data['result'] = "Erreur lors de l'enregistrement des données : " + str(e)
    else:
        data['result'] = 'Not Ajax'
    return JsonResponse(data)
