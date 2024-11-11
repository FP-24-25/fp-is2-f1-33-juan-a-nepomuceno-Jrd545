'''
Created on 24 oct 2024

@author: joaqu
'''

import math
import re
from collections import Counter

"""
Ejercicio A
"""
def P2(n:int, k:int, i:int = 1) -> int:
    if n < k or n <= 0 or k <= 0 or i <= 0 or i >= k + 1:
        raise ValueError("Parametros incorrectos")
    
    an:int = 1
    resultado:int = 1
    for n in range(i, k-2):
        an = (n-i+1)
        resultado *= an
       
    return resultado


"""
Ejercicio B
"""
def C2(n:int, k:int) -> float:
    if n <= k or n <= 0 or k <= 0:
        raise ValueError("Parametros incorrectos")
    
    solucion = (math.factorial(n))/(math.factorial(k+1)*math.factorial(n-(k+1)))
    return solucion


"""
Ejercicio C
"""
def combinatorio(n:int, k:int) -> float:
    if n < k:
        raise ValueError("Parametros incorrectos")
    
    resultado = (math.factorial(n))/(math.factorial(k)*math.factorial(n-k))
    return resultado

def  S2(n:int, k:int) -> float:
    if n < k or n <= 0 or k <= 0:
        raise ValueError("Parametros incorrectos")
    
    suma = 0
    for i in range(0, k):
        termino = ((-1)**i) * combinatorio(k, i) * (k-i)**(n+1)
        suma += termino
    
    resultado = (math.factorial(k)/(n*math.factorial(k+2))) * suma
    return resultado


"""
Ejercicio D
"""
def palabrasMasComunes(fichero:str, n:int= 5) -> list[tuple[str,int]]:
    if n <= 1:
        raise ValueError("Parametros incorrectos")
    
    try:
        with open(fichero, 'r', encoding='utf-8') as f:
            texto = f.read()

        palabras = re.findall(r'\b\w+\b', texto.lower())

        cuenta_palabras = Counter(palabras)
        palabras_repetidas = cuenta_palabras.most_common(n)

        return palabras_repetidas
        
        
    except IOError as e:
        return f"Error al intentar leer el archivo -> {e}"
    except Exception as e:
        return f"Error inesperado: {e}"
  
    
    
    
    
    
    
"""
Prueba de la funcion P2
"""
 
n = 4
k = 2  
i = 7
try:
    print("TEST DE LA FUNCIÓN P2:")
    print(f"Para n = {n}, k = {k} e i = {i} es: {P2(n, k,i)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n}, k = {k} e i = {i} sucede un error: {e}")

n = -12
k = 9  
i = 3
try:
    print(f"Para n = {n}, k = {k} e i = {i} es: {P2(n, k,i)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n}, k = {k} e i = {i} sucede un error: {e}")

n = 12
k = -9  
i = 3
try:
    print(f"Para n = {n}, k = {k} e i = {i} es: {P2(n, k,i)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n}, k = {k} e i = {i} sucede un error: {e}")
    
n = 12
k = 9  
i = -3
try:
    print(f"Para n = {n}, k = {k} e i = {i} es: {P2(n, k,i)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n}, k = {k} e i = {i} sucede un error: {e}")   
    
n = 12
k = 9  
i = 10
try:
    print(f"Para n = {n}, k = {k} e i = {i} es: {P2(n, k,i)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n}, k = {k} e i = {i} sucede un error: {e}") 

n = 12
k = 9  
i = 3
try:
    print(f"Para n = {n}, k = {k} e i = {i} es: {P2(n, k,i)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n}, k = {k} e i = {i} sucede un error: {e}")
    
print("|")  
print("|")  






"""
Prueba de la funcion C2
"""
 
n = 7
k = 9  
try:
    print("TEST DE LA FUNCIÓN C2:")
    print(f"Para n = {n} y k = {k} es: {C2(n, k)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n} y k = {k} sucede un error: {e}")
   
n = -12
k = 9  
try:
    print(f"Para n = {n} y k = {k} es: {C2(n, k)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n} y k = {k} sucede un error: {e}")
  
    
n = 12
k = -9  
try:
    print(f"Para n = {n} y k = {k} es: {C2(n, k)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n} y k = {k} sucede un error: {e}")

n = 12
k = 9  
try:
    print(f"Para n = {n} y k = {k} es: {C2(n, k)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n} y k = {k} sucede un error: {e}")

print("|")  
print("|") 







"""
Prueba de la funcion S2
"""
 
n = 2
k = 5  
try:
    print("TEST DE LA FUNCIÓN S2:")
    print(f"Para n = {n} y k = {k} es: {S2(n, k)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n} y k = {k} sucede un error: {e}")
    
n = -5
k = 4  
try:
    print(f"Para n = {n} y k = {k} es: {S2(n, k)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n} y k = {k} sucede un error: {e}") 
    
n = 5
k = -4  
try:
    print(f"Para n = {n} y k = {k} es: {S2(n, k)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n} y k = {k} sucede un error: {e}")
    
n = 5
k = 4  
try:
    print(f"Para n = {n} y k = {k} es: {S2(n, k)}")
except(TypeError, ValueError) as e:
    print(f"Para n = {n} y k = {k} sucede un error: {e}")
    
print("|")  
print("|")   











"""
Prueba de la funcion palabrasMasComunes
"""
 
nombre = "archivo_erroneo.txt"
n = 4
try:
    print("TEST DE LA FUNCIÓN palabrasMasComunes:")
    print(f"Para el archivo: {nombre} y n = {n} es: {palabrasMasComunes(nombre, n)}")
except(TypeError, ValueError) as e:
    print(f"Para el archivo: {nombre} y n = {n} sucede un error: {e}")
    
nombre = "archivo_erroneo.txt"
n = 0
try:
    print(f"Para el archivo: {nombre} y n = {n} es: {palabrasMasComunes(nombre, n)}")
except(TypeError, ValueError) as e:
    print(f"Para el archivo: {nombre} y n = {n} sucede un error: {e}")
    
nombre = "lin_quijote.txt"
n = 4
try:
    print(f"Para el archivo: {nombre} y n = {n} es: {palabrasMasComunes(nombre, n)}")
except(TypeError, ValueError) as e:
    print(f"Para el archivo: {nombre} y n = {n} sucede un error: {e}")
    
print("|")  
print("|")  