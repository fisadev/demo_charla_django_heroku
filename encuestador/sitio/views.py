from django.shortcuts import render
from django.http import JsonResponse

from sitio.models import Opcion, Respuesta


def home(request):
    opciones = Opcion.objects.all()
    return render(request, "home.html", {"opciones": opciones})


def api_responder(request, opcion_id):
    Respuesta.objects.create(opcion_id=opcion_id)
    return JsonResponse({"voto": "ok"})


def api_totales(request):
    return JsonResponse({"totales": Respuesta.totales()})
