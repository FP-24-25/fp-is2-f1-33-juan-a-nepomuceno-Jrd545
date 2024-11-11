'''
Created on 8 nov 2024

@author: joaqu
'''


from typing import Callable
from entrega2.tipos.Agregado_lineal import *

R = TypeVar("R")


class Lista_ordenada(Agregado_lineal[E], Generic[E,R]):
    
    def __init__(self, order: Callable[[E], R]):
        self._order = order
        self._elements: List[E] = []
        
    @staticmethod
    def of(order: Callable[[E], R]) -> "Lista_ordenada[E, R]":
        return Lista_ordenada(order)

    def _index_order(self, e: E) -> int:
        for i, current in enumerate(self._elements):
            if self._order(e) < self._order(current):
                return i
        return len(self._elements)  

    def add(self, e: E) -> None:
        index = self._index_order(e)
        self._elements.insert(index, e)

    def __str__(self) -> str:
        return "Lista_ordenada(" + ", ".join(str(e) for e in self._elements) + ")"
            
    
        
        
       
        