'''
Created on 17 oct 2024

@author: joaqu
'''

'''
Created on 17 oct 2024

@author: joaqu
'''

import math


#1
def producto1(n:int, k:int) -> int:
    if n <= k:
        raise ValueError("Parametros incorrectos")
    
    resultado = 1
    for i in range(0, k):
        resultado *= (n-i+1)  
    return resultado

n = 4
k = 2
try:
    print("################################################")
    print("TEST DE LA FUNCIÓN 1:")
    print(f"El producto de {n} y {k} es: {producto1(n,k)}")
except(TypeError, ValueError) as e:
    print(f"Error: {e}")
    












#2
def producto2(a1:int, r:int, k:int) -> int:
    
    an = 1
    resultado = 1
    for n in range(1, k+1):
        an = a1 * r**(n-1)
        resultado *= an
       
    return resultado

a1 = 3
r = 5
k = 2
try:
    print("################################################")
    print("TEST DE LA FUNCIÓN 2:")
    print(f"El producto de la secuencia geometrica con a1 = {a1}, r = {r} y k = {k} es: {producto2(a1, r, k)}")
except(TypeError, ValueError) as e:
    print(f"Error: {e}")
    












#3
def combinatorio(n:int, k:int) -> float:
    if n < k:
        raise ValueError("Parametros incorrectos")
    
    resultado = (math.factorial(n))/(math.factorial(k)*math.factorial(n-k))
    return resultado

n = 4
k = 2
try:
    print("################################################")
    print("TEST DE LA FUNCIÓN 3:")
    print(f"El numero combinatorio de {n} y {k} es: {combinatorio(n, k)}")
except(TypeError, ValueError) as e:
    print(f"Error: {e}")
    











  
#4
def S(n:int, k:int) -> float:
    if n < k:
        raise ValueError("Parametros incorrectos")
    
    suma = 0
    for i in range(k):
        termino = (-1)**i * combinatorio(k+1, i+1) * (k-i)**n
        suma += termino
    
    resultado = suma/math.factorial(k)
    return resultado

n = 4
k = 2  
try:
    print("################################################")
    print("TEST DE LA FUNCIÓN 4:")
    print(f"El numero S(n,k) de {n} y {k} es: {S(n, k)}")
except(TypeError, ValueError) as e:
    print(f"Error: {e}")
    











     
#5
def metodo_newton(f, f_der, a:float, e:float, iteraciones_max=100):
    x = a
    for _ in range(iteraciones_max):
        if abs(f_der(x)) == 0:
            raise ValueError("La derivada no puede ser cero")
        x = x - f(x)/f_der(x)
        if abs(f(x)) <= e:
            return x
def f(x):
    return 2*x**2

def f_der(x):
    return 4*x

error = 0.001
a = 3
try:
    print("################################################")
    print("TEST DE LA FUNCIÓN 5:")
    print(f"Resultado de la función 5, con a = {a}, e = {error}, f(x) = 2x^2 y f´(x) = 4x: {metodo_newton(f, f_der, a, error)}")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")



if __name__ == "__main__":
    pass