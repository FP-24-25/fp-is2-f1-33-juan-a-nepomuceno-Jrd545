'''
Created on 8 nov 2024

@author: joaqu
'''

from entrega2.tipos.Pila import *



print("TEST PILA:")
print(" ")
print("Método is_empty y size al crear una lista vacia:")
pila = Pila.of()
print("Resultado de usar el metodo is_empty:", pila.is_empty) 
print("Resultado de usar el metodo size:", pila.size) 

print(" ")
print("################################################")
print(" ")
pila = Pila.of()
pila.add(1)
pila.add(2)
pila.add(3)

print("Añadiendo 3 elementos, probamos el metodo size y elements:")
print("Resultado del metodo size:", pila.size)  
print("Resultado de usar el metodo elememts:", pila.elements)  


pila = Pila.of()
pila.add(1)
pila.add(2)
pila.add(3)

print(" ")
print("################################################")
print(" ")
print("Ahora probamos el metodo remove y remove_all al volver a poner el elemento iniciado:")
elemento = pila.remove()
print(f"Elemento eliminado: {elemento}")


pila = Pila.of()
pila.add(1)
pila.add(2)
pila.add(3)

elementos_eliminados = pila.remove_all()
print("Los elementos eliminados son", elementos_eliminados)
