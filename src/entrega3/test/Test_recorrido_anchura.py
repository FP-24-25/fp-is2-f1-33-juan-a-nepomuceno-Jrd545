'''
Created on 17 nov 2024

@author: belen
'''

from entrega3.Red_social import *
from entrega3.Recorrido_en_anchura import Recorrido_en_anchura

if __name__ == '__main__':
    rrss1: Red_social = Red_social.parse('resourcestest/usuarios.txt', 'resourcestest/relaciones.txt')
    r:Recorrido_en_anchura[Usuario,Relacion] = Recorrido_en_anchura.of(rrss1)
    
    source:Usuario = rrss1.usuarios_dni['25143909I']
    
    r.traverse(source)
    
    target: Usuario =  rrss1.usuarios_dni['87345530M']
    
    camino = r.path_to_origin(target)
    # Mostrar el resultado
    if target in camino:
        print(f"El camino más corto desde {source.dni} hasta {target.dni} es: {camino}")
        print(f"La distancia mínima es: {r.path_weight(target)} pasos.")
    else:
        print(f"No hay conexión directa entre {source.dni} y {target.dni}.")
    

    
    

    
    