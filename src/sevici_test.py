from sevici import *

estaciones_sevici = lee_estaciones('data/estaciones.csv')
mapa_estaciones = crea_mapa_estaciones(estaciones_sevici, color_azul)
mapa_estaciones.save("./out/azul.html")
