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

    












#2
def producto2(a1:int, r:int, k:int) -> int:
    an = 1
    resultado = 1
    for n in range(1, k+1):
        an = a1 * r**(n-1)
        resultado *= an
       
    return resultado
    











  
#3
def combinatorio(n:int, k:int) -> float:
    if n < k:
        raise ValueError("Parametros incorrectos")
    
    resultado = (math.factorial(n))/(math.factorial(k)*math.factorial(n-k))
    return resultado
    











    
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




if __name__ == "__main__":
    pass