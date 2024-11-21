'''
Created on 21 nov 2024

@author: Joaquín Ramos Díaz
'''

from entrega2.tipos.Agregado_lineal import *


class ColaConLimite(Agregado_lineal[E]):
    #Constructor
    def __init__(self, capacidad: int):
        super().__init__()
        assert capacidad > 0, "La capacidad debe ser mayor que 0"
        self.capacidad = capacidad
    
    #Método de factoria
    @staticmethod
    def of(capacidad: int) -> "ColaConLimite":
        return ColaConLimite(capacidad)

    #Método add
    def add(self, e: E) -> None:
        if self.is_full:
            raise OverflowError("La cola está llena.")
        self._elements.append(e)

    #Método is_full
    @property
    def is_full(self) -> bool:
        return len(self._elements) >= self.capacidad




#Las modificaciones del codigo agregado lineal estan realizadas dentro de entrega2.tipos.Agregado_lineal al final del tipo

#A partir de aquí voy a realizar todas las pruebas necesarias para comprobar el correcto funcionamiento del tipo
print("### Pruebas de la clase ColaConLimite con una cola vacia (metodo add y is_full) ###")
cola = ColaConLimite.of(3)

tarea = "Tarea 1"
try:
    cola.add(tarea)
    print(f"Elemento", tarea, "añadido correctamente")
    print("¿Está la cola llena?", cola.is_full)
except OverflowError as e:
    print(e)


print("\n### Pruebas de la clase ColaConLimite con una cola llena (metodo add y is_full) ###")
cola = ColaConLimite.of(3)
cola.add("Tarea 1")
cola.add("Tarea 2")
cola.add("Tarea 3")

try: 
    cola.add("Tarea 4")
except OverflowError as e:
    print(e)
    print("¿Está la cola llena?", cola.is_full)
    

print("\n### Pruebas del metodo remove ###")
cola = ColaConLimite.of(3)
cola.add("Tarea 1")
cola.add("Tarea 2")
cola.add("Tarea 3")

print(cola.remove())


print("\n### Pruebas de los metodos nuevos de Agregado_Lineal ###")
cola = ColaConLimite.of(5)

cola.add("Tarea 1")
cola.add("Tarea 2")
cola.add("Tarea 3")
cola.add("Tarea 4")
cola.add("Tarea 5")
print("\n### Prueba: Método contains ###")
print("¿Contiene la lista a Tarea 1?", cola.contains("Tarea 1"))  
print("¿Contiene la lista a Tarea 8?", cola.contains("Tarea 8")) 



print("\n### Prueba: Método find ###")
print(cola.find(lambda x: x.startswith("Tarea")))  
print(cola.find(lambda x: x == "Tarea 4")) 
print(cola.find(lambda x: x == "Tarea 8"))  



print("\n### Prueba: Método filter ###")
print(cola.filter(lambda x: "Tarea" in x)) 
print(cola.filter(lambda x: x.endswith("3"))) 
print(cola.filter(lambda x: x.startswith("8"))) 




