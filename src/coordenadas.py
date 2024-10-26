import math
from collections import namedtuple

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')
Estacion = namedtuple('Estacion', 'nombre, bornetas, bornetas_vacias, bicis_disponibles, coordenadas')

def calcula_distancia(coordenadas1, coordenadas2):
    x1 = coordenadas1.latitud
    x2 = coordenadas2.latitud
    y1 = coordenadas1.longitud
    y2 = coordenadas2.longitud
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

def estaciones_cercanas(estaciones, coordenadas, k=5):
    estaciones_cercanas = [
        (calcula_distancia(estacion.coordenadas, coordenadas), estacion.nombre, estacion.bicis_disponibles)
        for estacion in estaciones
    ]
    estaciones_cercanas.sort(key=lambda x: x[0])
    return estaciones_cercanas[:k]
