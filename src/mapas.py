from coordenadas import *
import folium

Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')
Estacion = namedtuple('Estacion', 'nombre, bornetas, bornetas_vacias, bicis_disponibles, coordenadas')

def crea_mapa(latitud, longitud, zoom=9):
    return folium.Map(location=[latitud, longitud], zoom_start=zoom)

def crea_marcador(latitud, longitud, etiqueta, color):
    return folium.Marker(
        [latitud, longitud], popup=etiqueta, icon=folium.Icon(color=color, icon='info-sign')
    )

def color_azul(estacion):
    return "blue"

def obten_color_bicis_disponibles(estacion):
    res = "red"
    if estacion.bicis_disponibles > 0:
        res = "green"
    return res
