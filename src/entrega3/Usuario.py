'''
Created on 17 nov 2024

@author: Joaquín Ramos Díaz
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
import re


@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    
    @staticmethod
    def of(dni:str, nombre:str, apellidos:str, fecha_nacimiento:date) -> Usuario:
        # Validación del formato del DNI
        if not re.match(r'\d{8}[A-Za-z]', dni):
            raise ValueError("El DNI no tiene el formato válido")
        # Verificar que la fecha de nacimiento es anterior a la fecha actual
        if fecha_nacimiento >= date.today():
            raise ValueError("La fecha de nacimiento no puede ser posterior o igual a la fecha actual")
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)
    
    
    @staticmethod
    def parse(linea:str) -> Usuario:
        # Parsear la cadena con el formato esperado: "45718832U,Carlos,Lopez,1984-01-14"
        parts = linea.split(",")
        if len(parts) != 4:
            raise ValueError("La cadena no tiene el formato correcto")
        dni, nombre, apellidos, fecha_nacimiento_str = parts
        # Convertir la fecha de nacimiento a un objeto de tipo date
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
        return Usuario.of(dni, nombre, apellidos, fecha_nacimiento)
        
    def __str__(self):
        # Representación como cadena: dni - nombre
        return f"{self.dni} - {self.nombre}"

if __name__ == '__main__':
    linea:str = "45718832U,Carlos,Lopez,1984-01-14"
    usuario: Usuario = Usuario.parse(linea)
    print(usuario)