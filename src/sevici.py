import csv
from collections import namedtuple
from mapas import *

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')
Estacion = namedtuple('Estacion', 'nombre, bornetas, bornetas_vacias, bicis_disponibles, coordenadas')

def lee_estaciones(fichero):
    estaciones = []
    with open(fichero, encoding='utf-8') as file:
        lector_csv = csv.reader(file)
        next(lector_csv)
        for linea in lector_csv:
            nombre = linea[0]
            bornetas = int(linea[1])
            bornetas_vacias = int(linea[2])
            bicis_disponibles = int(linea[3])
            coordenada_1 = float(linea[4])
            coordenada_2 = float(linea[5])
            coordenadas = Coordenadas(latitud=coordenada_1, longitud=coordenada_2)
            estacion = Estacion(nombre=nombre, bornetas=bornetas, bornetas_vacias=bornetas_vacias,
                                bicis_disponibles=bicis_disponibles, coordenadas=coordenadas)
            estaciones.append(estacion)
    return estaciones

def estaciones_bicis_libres(estaciones, k=5):
    estacion_con_al_menos_k_bicicletas_libres = [
        (estacion.bicis_disponibles, estacion.nombre) 
        for estacion in estaciones if estacion.bicis_disponibles >= k
    ]
    estacion_con_al_menos_k_bicicletas_libres.sort(key=lambda x: x[0])
    return estacion_con_al_menos_k_bicicletas_libres

def media_coordenadas(estaciones):
    latitud = sum(estacion.coordenadas.latitud for estacion in estaciones) / len(estaciones)
    longitud = sum(estacion.coordenadas.longitud for estacion in estaciones) / len(estaciones)
    return Coordenadas(latitud, longitud)

def crea_mapa_estaciones(estaciones, funcion_color):
    centro_mapa = media_coordenadas(estaciones)
    mapa = crea_mapa(centro_mapa.latitud, centro_mapa.longitud, 13)

    for estacion in estaciones:
        etiqueta = estacion.nombre
        color = funcion_color(estacion)
        marcador = crea_marcador(estacion.coordenadas.latitud, estacion.coordenadas.longitud, etiqueta, color)
        marcador.add_to(mapa)

    return mapa
