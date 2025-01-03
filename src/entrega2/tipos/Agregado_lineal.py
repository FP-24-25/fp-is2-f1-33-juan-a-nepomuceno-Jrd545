'''
Created on 8 nov 2024

@author: joaquín Ramos Díaz
'''

from __future__ import annotations
from typing import List, Generic, TypeVar, Callable
from abc import ABC, abstractmethod


E = TypeVar("E") 

class Agregado_lineal(ABC, Generic[E]):
    
    def __init__(self):
        self._elements: List[E] = []
    
    #Propiedades
    @property
    def size(self) -> int:
        return len(self._elements)
    
    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    @property
    def elements(self) -> List[E]:
        return self._elements.copy()
    
    #Métodos
    @abstractmethod
    def add(self, e: E) -> None:
        pass
    
    def add_all(self, ls: list[E]) -> None:
        for e in ls:
            self.add(e)
    
    def remove(self) -> E: 
        assert len(self._elements) > 0, "El agregado está vacío"
        return self._elements.pop(0)
    
    def remove_all(self) -> list[E]:
        elementos_eliminados = self._elements.copy()
        self._elements.clear()
        return elementos_eliminados
    
    
    #Modificacion del codigo:
    
    #Metodo contains
    def contains(self, e: E) -> bool:
        return e in self._elements
    
    #Metodo find
    def find(self, func: Callable[[E], bool]) -> E | None:
        for e in self._elements:
            if func(e):
                return e
        return None
    
    #Metodo filter
    def filter(self, func: Callable[[E], bool]) -> list[E]:
        return [e for e in self._elements if func(e)]
    