'''
Created on 8 nov 2024

@author: joaquín Ramos Díaz
'''

from entrega2.tipos.Lista_ordenada_sin_repeticion import *
    
    
    
print("TEST DE LISTA ORDENADA SIN REPETICIÓN:")
print(" ")
print("################################################")
print(" ")

lista = Lista_ordenada_sin_repeticion.of(lambda x: -x)
print("Creación de una lista con criterio de orden lambda x: -x")


elementos_para_añadir = [23, 47, 47, 1, 2, -3, 4, 5]
for elem in elementos_para_añadir:
    lista.add(elem)

print(f"Se añade en este orden: {', '.join(map(str, elementos_para_añadir))}")
print(f"Resultado de la lista ordenada sin repetición: {lista}")

print(" ")
print("################################################")
print(" ")


elemento_eliminado = lista.remove()
print(f"El elemento eliminado al utilizar remove(): {elemento_eliminado}")

print(" ")
print("################################################")
print(" ")

lista.add(47)
elementos_eliminados = lista.remove_all()
print(f"Elementos eliminados utilizando remove_all: {elementos_eliminados}")

print(" ")
print("################################################")
print(" ")

print("Comprobando si se añaden los números en la posición correcta...")

for elem in [23, 47, 5, 4, 2, 1, -3]:
    lista.add(elem)

lista.add(0)
print(f"Lista después de añadirle el 0: {lista}")
lista.add(0)
print(f"Lista después de añadirle el 0: {lista}")
lista.add(7)
print(f"Lista después de añadirle el 7: {lista}")
    
    
