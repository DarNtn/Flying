from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import *
from django.template.loader import get_template


def index(request):

	airports=Airports.objects.order_by('+name')
	
	contenido = {
     'airports': airports,
     }
	return render (request,"formulario.html",contenido)

def search(request):
	if request.method == 'POST':
		airports=Airports.objects.all()

		contenido={"airports":airports}
		
		origen = Airports.objects(name=request.POST["origen"]).first()
		destino = Airports.objects(name=request.POST["destino"]).first()
		stops = int(request.POST["tipo"])
		print(request.POST)

		contenido["origen"]=origen
		contenido["destino"]=destino
		if stops==0:
			contenido["tipo"]="Sin"
		else:
			contenido["tipo"]="Con"

		#size = db.routes.find({"sAirport":origen, "dAirport":destino, "stops":stops}).count()
		rutas = Routes.objects(sAirport=origen.iata, dAirport=destino.iata, stops=stops)
		print(rutas)
		contenido["rutas"]=rutas
		if(rutas.count() > 0):
			#return HttpResponse(template.render(RequestContext(request,{'origenes':origenes, 'destinos':destinos, 'rutas':rutas})))	
			#contenido = {'origen':origen, 'destino': destino, 'resultados':rutas}
			return render(request, 'resultados.html',contenido)
		else:
			#return HttpResponse(template.render(RequestContext(request,{'origenes':origenes, 'destinos':destinos})))
			return render(request, 'vacio.html', contenido)

