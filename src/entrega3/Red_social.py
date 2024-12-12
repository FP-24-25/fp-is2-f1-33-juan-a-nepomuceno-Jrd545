'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from entrega3.E_grafo import E_grafo, Graph_type, Traverse_type
from entrega3.Usuario import Usuario
from entrega3.Relacion import Relacion
from us.lsi.tools.File import lineas_de_fichero, absolute_path
from datetime import date

# Esta clase se debe ejecutar (ver el main abajo del todo)

class Red_social(E_grafo[Usuario, Relacion]):
    
    def __init__(self,graph_type:Graph_type,traverse_type:Traverse_type)->None:
        super().__init__(graph_type, lambda r: r.interacciones, traverse_type)
        self.__usuarios_dni:dict[str,Usuario] = {}
        
    
    @staticmethod
    def of(graph_type: Graph_type = Graph_type.UNDIRECTED, traverse_type: Traverse_type = Traverse_type.BACK) -> Red_social: 
        # Crear una nueva instancia de Red_social con los parámetros dados
        return Red_social(graph_type, traverse_type)
    
    @staticmethod
    def parse(f1: str, f2: str, graph_type: Graph_type = Graph_type.UNDIRECTED, traverse_type: Traverse_type = Traverse_type.BACK) -> Red_social:
        rrss = Red_social.of(graph_type, traverse_type)

        # Leer y cargar usuarios
        for linea in lineas_de_fichero(f1):
            try:
                # Leer usuario y crear instancia de Usuario
                dni, nombre, apellidos, fecha_nacimiento = linea.strip().split(',')
                usuario = Usuario.of(dni, nombre, apellidos, date.fromisoformat(fecha_nacimiento))  # Usa date
                rrss.add_vertex(usuario)  # Agregar al grafo
                rrss.usuarios_dni[dni] = usuario  # Guardar en el diccionario
            except Exception as e:
                pass

            # Leer y cargar relaciones evitando duplicados
            relaciones_existentes = []  # Para rastrear relaciones únicas
            for linea in lineas_de_fichero(f2):
                try:
                    dni1, dni2, interacciones, dias_activa = linea.strip().split(',')
                    interacciones = int(interacciones)
                    dias_activa = int(dias_activa)

                    # Verificar si ambos usuarios existen en el diccionario
                    if dni1 not in rrss.usuarios_dni or dni2 not in rrss.usuarios_dni:
                        continue  # Ignorar la relación si no se encuentran ambos usuarios

                    # Verificar si la relación ya existe
                    if any((dni1 == r[0] and dni2 == r[1]) or (dni1 == r[1] and dni2 == r[0]) for r in relaciones_existentes):
                        continue  # Ignorar relaciones duplicadas

                    # Agregar relación a la lista de relaciones únicas
                    relaciones_existentes.append((dni1, dni2))

                    # Crear usuarios y la relación
                    usuario1 = rrss.usuarios_dni[dni1]
                    usuario2 = rrss.usuarios_dni[dni2]
                    relacion = Relacion.of(interacciones, dias_activa)  # Crear la relación
                    rrss.add_edge(usuario1, usuario2, relacion)  # Agregar la relación al grafo

                except Exception as e:
                    pass
        # Convertir vértices a lista ordenada
        rrss._vertex_set = list(sorted(rrss._vertex_set, key=lambda v: v.dni))
        # Convertir aristas a lista ordenada (si es necesario)
        rrss._edge_set = list(sorted(rrss._edge_set, key=lambda e: (
            rrss.edge_source(e).dni, rrss.edge_target(e).dni
            )))

        return rrss

    @property
    def usuarios_dni(self)->dict[str,Usuario]:
        return self.__usuarios_dni



if __name__ == '__main__':
    rrss: Red_social = Red_social.parse(absolute_path('resources/usuarios.txt'), absolute_path('resources/relaciones.txt'))
    print(rrss.plot_graph())
    #print(rrss)
   