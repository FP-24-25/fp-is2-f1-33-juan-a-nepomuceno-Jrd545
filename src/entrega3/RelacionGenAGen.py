'''
Created on 19 dic 2024

@author: joaqu
'''

from __future__ import annotations
from typing import TypeVar
from dataclasses import dataclass

@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> RelacionGenAGen:
        if not -1.0 <= conexion <= 1.0:
            raise ValueError("La conexión debe estar entre -1 y 1, ambos incluidos.")
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def parse(cadena: str) -> RelacionGenAGen:
        partes = cadena.split(",")
        if len(partes) != 3:
            raise ValueError("La cadena debe tener exactamente tres elementos separados por comas.")
        
        nombre_gen1, nombre_gen2, conexion_str = partes
        try:
            conexion = float(conexion_str)
        except ValueError:
            raise ValueError("El valor de conexión debe ser un número real.")
        
        return RelacionGenAGen.of(nombre_gen1.strip(), nombre_gen2.strip(), conexion)

    @property
    def coexpresados(self) -> bool:
        return self.conexion > 0.75

    @property
    def antiexpresados(self) -> bool:
        return self.conexion < -0.75

    def __str__(self) -> str:
        return f"{self.nombre_gen1}-{self.nombre_gen2}: conexión={self.conexion:.2f}"


if __name__ == "__main__":
    relaciones_data = "TP53,EGFR,0.5"
    relaciones = [RelacionGenAGen.parse(line) for line in relaciones_data.strip().split('\n')]

    for relacion in relaciones:
        print(relacion)
        print(f"  Coexpresados: {relacion.coexpresados}")
        print(f"  Antiexpresados: {relacion.antiexpresados}")