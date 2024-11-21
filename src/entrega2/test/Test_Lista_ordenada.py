'''
Created on 8 nov 2024

@author: joaquín Ramos Díaz
'''

from entrega2.tipos.Lista_ordenada import *
        

print("TEST DE LISTA ORDENADA:")
print(" ")

lista = Lista_ordenada.of(lambda x: x)
print("Creación de una lista con criterio de orden lambda x: x")


print("Se añade en este orden: 3, 1, 2")
lista.add(3)
lista.add(1)
lista.add(2)
print(f"Resultado de la lista: {lista}")

print(" ")
print("################################################")
print(" ")
removed_element = lista.remove()
print(f"El elemento eliminado al utilizar remove(): {removed_element}")

print(" ")
print("################################################")
print(" ")

lista.add(1)
removed_all = lista.remove_all()
print(f"Elementos eliminados utilizando remove_all: {removed_all}")

print(" ")
print("################################################")
print(" ")
print("Comprobando si se añaden los números en la posición correcta...")

lista.add(1)
lista.add(2)
lista.add(3)
lista.add(0)
print(f"Lista después de añadirle el 0: {lista}")

lista.add(10)
print(f"Lista después de añadirle el 10: {lista}")

lista.add(7)
print(f"Lista después de añadirle el 7: {lista}")

       
        