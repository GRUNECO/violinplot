"""
Potencias
|estudio   |canal|banda|potencia|
|nestudios |     |     |        |
* todos sujetos, 1 estudio  1G todas las bandas sin distinguir el canal|7 
* todos sujetos, 1 estudio  1G 1 banda por canal | 1x58 
* todos sujetos, n estudios 1G  1 bandas sin distinguir el canal| nx1x1 
* todos sujetos, n estudios 1G  1 bandas por canal| nx1x1 
* para 1 sujeto (reporte individual)

Reject
* todos sujetos, 1 estudio sin distinguir el canal
* todos sujetos, 1 estudio banda por canal
*
*

# GRUPO
* 1 estudio todos los pertenecientes a 1G, 7 bandas sin distinguir el canal:ok
* n estudios todos los pertenecientes a 1G, 7 bandas sin distinguir el canal: ok
* 1 estudio, n grupos, 7 bandas sin distinguir el canal

#VISITA
* 1 estudio 1 visita, 7 bandas 
* n estudio 1 visita, 7 bandas


Dudas
*si por estudio no tiene sentido hacer comparaciones porque no están todos en reposo, 
que sentido tiene comparar todos los datos de un estudio
*por visitas se tiene en cuenta todos los grupos? o tiene que ser para una visita y un 
grupo en especifico 


Observaciones:
* mejorar los dataframes, agregarle una columna de grupo 
* mejorar col y row 
* mejorar get_dataframes
* organizar images_nS_7B_power para que salga por columnas y por filas 
* organizar para que le entren listas de grupos compare_nS_1G_1B
"""

