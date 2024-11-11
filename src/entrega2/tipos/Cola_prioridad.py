'''
Created on 8 nov 2024

@author: joaqu
'''

from __future__ import annotations
from typing import List, Generic, TypeVar, Tuple


E = TypeVar('E')  
P = TypeVar('P')  

class Cola_de_prioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[E] = []      
        self._priorities: List[P] = []    

    @staticmethod
    def of() -> 'Cola_de_prioridad[E, P]':
        return Cola_de_prioridad()

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    @property
    def elements(self) -> List[E]:
        return self._elements.copy()

    def _index_order(self, priority: P) -> int:
        pos = 0
        while pos < len(self._priorities) and self._priorities[pos] <= priority:
            pos += 1
        return pos

    def add(self, e: E, priority: P) -> None:
        pos = self._index_order(priority)  
        self._elements.insert(pos, e)
        self._priorities.insert(pos, priority)

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        for e, priority in ls:
            self.add(e, priority)

    def remove(self) -> E:
        assert len(self._elements) > 0, "El agregado está vacío"
        self._priorities.pop(0)
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        elementos_eliminados = []
        while not self.is_empty:
            elementos_eliminados.append(self.remove())
        return elementos_eliminados

    def decrease_priority(self, e: E, new_priority: P) -> None:
        index = self.index_of(e)
        if index != -1 and new_priority < self._priorities[index]:
            self._elements.pop(index)
            self._priorities.pop(index)
            self.add(e, new_priority)

    def __str__(self) -> str:
        elementos = ', '.join(f"({e}, {p})" for e, p in zip(self._elements, self._priorities))
        return f"ColaPrioridad[{elementos}]"

