from django.shortcuts import render
from AppFlia.models import Familiares
from django.http import HttpResponse
import datetime
from django.template import Context, Template, loader

# Create your views here.

def cargo_fliar1(self):
    # cargo familiar 1
    nombre_asig="Horacio Manzoni"
    relacion_asig="Padre"
    fecha_nac_asig=datetime.date(1945, 11, 27)
    mayor_de_edad_asig=True

    fliar=Familiares(nombre=nombre_asig, relacion=relacion_asig, fecha_nac=fecha_nac_asig, mayor_de_edad=mayor_de_edad_asig )
    fliar.save()
    texto=f"Familiar creado: {fliar.nombre} - {fliar.relacion}"
    diccionario1={'nombre':nombre_asig,'relacion':relacion_asig,'fecha_nac':fecha_nac_asig,'mayor_de_edad':mayor_de_edad_asig}
    
    plantilla=loader.get_template('template1.html')
    
    documento=plantilla.render(diccionario1)
    
    return HttpResponse(documento)

def cargo_fliar2(self):
    # cargo familiar 2
    nombre_asig="Stella Guida"
    relacion_asig="Madre"
    fecha_nac_asig=datetime.date(1948, 10, 16)
    mayor_de_edad_asig=True

    fliar=Familiares(nombre=nombre_asig, relacion=relacion_asig, fecha_nac=fecha_nac_asig, mayor_de_edad=mayor_de_edad_asig )
    fliar.save()
    texto=f"Familiar creado: {fliar.nombre} - {fliar.relacion}"
    diccionario1={'nombre':nombre_asig,'relacion':relacion_asig,'fecha_nac':fecha_nac_asig,'mayor_de_edad':mayor_de_edad_asig}
    
    plantilla=loader.get_template('template1.html')
    
    documento=plantilla.render(diccionario1)
    
    return HttpResponse(documento)

def cargo_fliar3(self):
    # cargo familiar 3
    nombre_asig="Debora Ballaratti"
    relacion_asig="Esposa"
    fecha_nac_asig=datetime.date(1972, 3, 23)
    mayor_de_edad_asig=True

    fliar=Familiares(nombre=nombre_asig, relacion=relacion_asig, fecha_nac=fecha_nac_asig, mayor_de_edad=mayor_de_edad_asig )
    fliar.save()
    texto=f"Familiar creado: {fliar.nombre} - {fliar.relacion}"
    diccionario1={'nombre':nombre_asig,'relacion':relacion_asig,'fecha_nac':fecha_nac_asig,'mayor_de_edad':mayor_de_edad_asig}
    
    plantilla=loader.get_template('template1.html')
    
    documento=plantilla.render(diccionario1)
    
    return HttpResponse(documento)