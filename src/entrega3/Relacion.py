'''
Created on 17 nov 2024

@author: Joaquín Ramos Díaz
'''
from __future__ import annotations
from dataclasses import dataclass



@dataclass(frozen=True)
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    # El contador interno se maneja de manera privada
    __xx_num: int = 0
    
    @staticmethod
    def of(interacciones: int, dias_activa: int)->Relacion:
        # Incrementar el contador para asegurar un ID único
        Relacion.__xx_num += 1
        # Crear una nueva instancia de Relacion con un ID único
        return Relacion(Relacion.__xx_num, interacciones, dias_activa)
    
    def __str__(self):
        # Representación en el formato especificado
        return f"({self.id} - días activa: {self.dias_activa} - num interacciones {self.interacciones})"
    

if __name__ == '__main__':
    pass