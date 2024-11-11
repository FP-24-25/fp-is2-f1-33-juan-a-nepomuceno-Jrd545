'''
Created on 8 nov 2024

@author: joaqu
'''

from entrega2.tipos.Agregado_lineal import *

R = TypeVar("R")


class Cola(Agregado_lineal[E]):

    @staticmethod
    def of() -> 'Cola[E]':
        return Cola()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __str__(self) -> str:
        elementos = ', '.join(str(e) for e in self._elements)
        return f"Cola({elementos})"
        
    
    
    
    
    
    
    