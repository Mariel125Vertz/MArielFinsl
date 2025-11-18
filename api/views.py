from django.shortcuts import render
import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'notebooks'))
from kdd_processing import generar_graficas

def graficas(request):
    archivos = generar_graficas()  # Devuelve lista de nombres de imágenes
    return render(request, 'api/graficas.html', {'archivos': archivos})
