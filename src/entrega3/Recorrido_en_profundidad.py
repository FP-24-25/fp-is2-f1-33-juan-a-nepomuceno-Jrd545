'''
Created on 17 nov 2024

@author: Joaquín Ramos Díaz
'''

from __future__ import annotations
from typing import TypeVar
from entrega3.Grafo import Grafo
from entrega2.tipos.Pila import Pila
from entrega3.Recorrido import Recorrido

V = TypeVar('V')
E = TypeVar('E')

class Recorrido_en_profundidad(Recorrido[V, E]):

    @staticmethod
    def of(grafo: Grafo[V, E]) -> Recorrido_en_profundidad[V, E]:
        return Recorrido_en_profundidad(grafo)

    def __init__(self, grafo: Grafo[V, E]) -> None:
        super().__init__(grafo)
        self._grafo = grafo  # Inicializamos el grafo
        self._path = []  # Inicializamos el recorrido
        self._tree = {}  # Inicializamos el árbol de recorrido

    def traverse(self, source: V) -> None:
        v: V = source
        stack: Pila[V] = Pila.of()
        stack.add(v)
        self._tree[v] = (None, 0)  # Marcamos el vértice fuente con predecesor None y costo 0

        while len(stack._elements) > 0:  # Comprobamos si la pila no está vacía
            v = stack.remove()  # Extraemos el vértice en la parte superior de la pila
            self._path.append(v)  # Lo agregamos al recorrido

            for neighbor in self._grafo.successors(v):  # Iteramos sobre los sucesores
                if neighbor not in self._tree:  # Si el vecino no ha sido visitado
                    stack.add(neighbor)  # Lo agregamos a la pila
                    self._tree[neighbor] = (v, self._tree[v][1] + 1)  # Registramos su predecesor y el costo

if __name__ == '__main__':
    pass
