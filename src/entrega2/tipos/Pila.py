'''
Created on 8 nov 2024

@author: joaqu
'''

from __future__ import annotations
from entrega2.tipos.Agregado_lineal import *



class Pila(Agregado_lineal[E]):
    
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def of() -> Pila[E]:
        return Pila()

    def add(self, e: E) -> None:
        self._elements.insert(0, e)  
