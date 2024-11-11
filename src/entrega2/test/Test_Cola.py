'''
Created on 8 nov 2024

@author: joaqu
'''

from entrega2.tipos.Cola import *
    
    
print("TEST DE COLA:")
print(" ")
print("################################################")
print(" ")
    
cola = Cola.of()
    
elementos_a_agregar = [23, 47, 1, 2, -3, 4, 5]
cola.add_all(elementos_a_agregar)
    
print("Creación de una cola vacía a la que luego se le añaden con un solo método los números:", elementos_a_agregar)
print("Resultado de la cola:", cola)
print(" ")
print("################################################")
print(" ") 

elementos_eliminados = cola.remove_all()
print("Elementos eliminados utilizando remove_all:", elementos_eliminados)
    
    