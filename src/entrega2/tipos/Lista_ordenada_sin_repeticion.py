'''
Created on 8 nov 2024

@author: joaqu
'''


from typing import Callable
from entrega2.tipos.Agregado_lineal import *

R = TypeVar("R")


class Lista_ordenada_sin_repeticion(Agregado_lineal[E], Generic[E, R]):

    def __init__(self, order: Callable[[E], R]):
        self._order = order
        self._elements: List[E] = []

    @staticmethod
    def of(order: Callable[[E], R]) -> 'Lista_ordenada_sin_repeticion[E, R]':
        return Lista_ordenada_sin_repeticion(order)

    def __index_order(self, e: E) -> int:
        for i, elem in enumerate(self._elements):
            if self._order(e) < self._order(elem):
                return i
        return len(self._elements)

    def add(self, e: E) -> None:
        if e not in self._elements: 
            index = self.__index_order(e)
            self._elements.insert(index, e)

    def __repr__(self) -> str:
        elements_str = ', '.join(repr(e) for e in self._elements)
        return f"ListaOrdenadaSinRepeticion({elements_str})"
    
    
    
    
    
    
    
    
