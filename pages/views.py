from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from request.models import *
from django.http import FileResponse
from django.urls import reverse

class HomePageView(TemplateView):
    template_name = 'home.html'

def fetch(request):
    if request.method == "GET":
        documentos = request.GET["documentos"]
        serie = request.GET["serie"]
        correlativo = request.GET["correlativo"]
        fecha = request.GET["fecha"]
        monto = request.GET["monto"]
    fetch_document = Request.objects.filter(documento = documentos, serie = serie, correlativo = correlativo, fecha = fecha, monto = monto)
    fetch_document = fetch_document.first()

    if fetch_document:
        file_path = str(fetch_document.archivo)
        return render(request, "home.html", {"file_path": file_path, "found": "found", "done": "done"})
    else:
        return render(request, "home.html", {"not_found": "not_found", "done": "done"})

def serve(request):
    try:
        download = request.GET["download"]
        response = FileResponse(open(download, 'rb'), as_attachment=True)  
    except:
        view = request.GET["view"]
        response = FileResponse(open(view, 'rb'))
    return response
