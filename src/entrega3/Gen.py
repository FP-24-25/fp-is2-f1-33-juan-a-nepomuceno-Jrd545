'''
Created on 19 dic 2024

@author: joaqu
'''

from __future__ import annotations
from dataclasses import dataclass



@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosomas: str

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosomas: str) -> Gen:
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser mayor o igual a 0.")
        return Gen(nombre, tipo, num_mutaciones, loc_cromosomas)

    @staticmethod
    def parse(gen_str: str) -> Gen:
        try:
            nombre, tipo, num_mutaciones, loc_cromosomas = gen_str.strip("()").split(",")
            return Gen.of(
                nombre.strip(),
                tipo.strip(),
                int(num_mutaciones.strip()),
                loc_cromosomas.strip()
            )
        except ValueError:
            raise ValueError("El formato de la cadena no es válido. Debe ser (nombre,tipo,num_mutaciones,loc_cromosomas).")

    def __str__(self) -> str:
        return f"{self.nombre}: ({self.tipo},{self.num_mutaciones},{self.loc_cromosomas})"


if __name__ == '__main__':
    # Prueba del método parse
    try:
        gen_str = "TP53,supresor tumoral,256,17p13.1"
        gen = Gen.parse(gen_str)
        print(gen)  # TP53: (supresor tumoral,256,17p13.1)
    except ValueError as e:
        print(f"Error al parsear el gen: {e}")
    
    # Prueba de restricciones
    try:
        gen_erroneo = Gen.of("BRCA1", "reparador ADN", -5, "17q21")
        print(gen_erroneo)
    except ValueError as e:
        print(f"Error al crear el gen: {e}")  # Error esperado: El número de mutaciones debe ser mayor o igual a 0.
