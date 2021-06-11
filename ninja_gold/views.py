from django.shortcuts import redirect, render, HttpResponse
import random #para generar numero aleatorios
from time import gmtime, strftime, localtime
from datetime import datetime

def index(request):
    if 'counter_gold' not in request.session:
        request.session['counter_gold'] = 0

    if 'activities' not in request.session:
        request.session['activities'] = []

    if 'winCantGold' not in request.session:
        request.session['winCantGold'] = 0    
    
    if 'loseMov' not in request.session:
         request.session['loseMov'] = 0  

    if 'cantMov' not in request.session:
         request.session['cantMov'] = 0 
         
    request.session['winCantGold']  = 150 #para configuración del usuario
    request.session['loseMov'] = 10 #para configuración del usuario

    return render(request,'index.html')

def processMoney(request,ubicacion):
    aleatorio = 0 #almacenara un número generado de forma aleatoria
    mensaje = "" #para almacenar el mensaje que se mostrará al usuario en el template
    color = "" #para almacenar el color con el que se mostrará el mensaje, puede ser ver si aleatorio > 0 o rojo si aleatorio > 0
    #La ubicación es donde el ninja va a buscar oro, en esta ocación se está pasando por la url -> ver urls.py
    
    if request.method == "POST": # preguntamos si el metodo del formulario es POST
        #dependiendo de la ubicación (formulario) en la que se realizó el clic vamos a una u otra opción
        if ubicacion == 'farm':
                    aleatorio = random.randint(10, 20)
                    request.session['counter_gold'] += aleatorio
                    mensaje = (f'Earned {aleatorio} golds from the farm ({datetime.now().strftime("%D %H:%M:%S")})')
                    color = mensajeEstado(aleatorio)
                    request.session['cantMov'] += 1
                    #print(request.session['cantMov'])

        elif ubicacion == 'cave':
                    aleatorio = random.randint(5, 10)
                    request.session['counter_gold'] += aleatorio 
                    mensaje = (f'Earned {aleatorio} golds from the cave ({datetime.now().strftime("%D %H:%M:%S")})')
                    color = mensajeEstado(aleatorio)
                    request.session['cantMov'] += 1
                    #print(request.session['cantMov'])

        elif ubicacion == 'house':
                    aleatorio = random.randint(2, 20)
                    request.session['counter_gold'] += aleatorio 
                    mensaje = (f'Earned {aleatorio} golds from the house ({datetime.now().strftime("%D %H:%M:%S")})')
                    color = mensajeEstado(aleatorio)
                    request.session['cantMov'] += 1
                    #print(request.session['cantMov'])

        elif ubicacion == 'casino':
                    aleatorio = random.randint(-50, 50)
                    request.session['counter_gold'] += aleatorio
                    mensaje = (f'Earned {aleatorio} golds from the casino ({datetime.now().strftime("%D %H:%M:%S")})')
                    color = mensajeEstado(aleatorio)
                    request.session['cantMov'] += 1
                    #print(request.session['cantMov'])

        texto = {
           "mensaje": mensaje, 
           "color" : color
        }  

        request.session['activities'].insert(0,texto)
        request.session.save()          
    
    return redirect('/')

def resetCounterGold(request):
    del request.session['counter_gold']
    del request.session['activities']
    del request.session['winCantGold']
    del request.session['loseMov']
    del request.session['cantMov']

    return redirect("/")

def mensajeEstado(aleatorio):
    if aleatorio > 0:
        color = "verde"
    else:
        color = "rojo"

    return color
