'''
Created on 17 nov 2024

@author: Joaquín Ramos Díaz
'''
from __future__ import annotations
from typing import TypeVar
from entrega3.Grafo import Grafo
from entrega2.tipos.Cola import Cola
from entrega3.Recorrido import Recorrido

V = TypeVar('V')
E = TypeVar('E')


class Recorrido_en_anchura(Recorrido[V,E]):
    
    @staticmethod
    def of(grafo:Grafo[V,E])->Recorrido_en_anchura[V,E]:
        return Recorrido_en_anchura(grafo)
    
    def __init__(self,grafo:Grafo[V,E])->None:
        super().__init__(grafo)
        self._grafo = grafo  # Inicializar el grafo
        self._path = []  # Inicializar el recorrido
        self._tree = {}  # Inicializar el árbol de recorrido
    
    def traverse(self,source:V)->None:
        v:V = source
        q:Cola[V] = Cola.of()
        q.add(v)
        self._tree[v] = (None,0)
        
        while len(q._elements) > 0:  # Cambiar de is_empty() a comprobar si la lista de elementos está vacía
            v = q.remove()  # Extraemos el vértice en la parte superior de la cola
            self._path.append(v)  # Lo agregamos al recorrido

            for neighbor in self._grafo.successors(v):  # Iteramos sobre los sucesores
                if neighbor not in self._tree:  # Si el vecino no ha sido visitado
                    q.add(neighbor)  # Lo agregamos a la cola
                    self._tree[neighbor] = (v, self._tree[v][1] + 1)  # Registramos su predecesor y el costo

if __name__ == '__main__':
    pass