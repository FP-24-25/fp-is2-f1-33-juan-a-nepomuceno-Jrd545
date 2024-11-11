'''
Created on 17 oct 2024

@author: joaqu
'''

import re
from typing import Optional


#6
def contar_palabra(fichero: str, sep: str, cad: str):
    try:
        contador = 0
        with open(fichero, 'r', encoding='utf-8') as f:
            for linea in f:
                cad = (cad.lower()).capitalize()
                palabras = re.split(sep, linea)
                palabras = [palabra.lower() for palabra in palabras]
                palabras = [palabra.capitalize() for palabra in palabras]
                for palabra in palabras:
                    if palabra == cad:
                        contador += 1
        return contador

    except IOError as e:
        return f"Error al intentar leer el archivo: {e}"
    except Exception as i:
        return f"Error inesperado: {i}"

direc = "C:/Users/joaqu/git/entrega1-proyecto-Jrd545/src/resources/lin_quijote.txt"
cad = "hidalgo"
try:
    print("################################################")
    print("TEST DE LA FUNCIÓN 6:")
    print("El número de veces que aparece la palabra", cad, "son:", contar_palabra(direc, r"[ ,\n]+", cad))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
    











   
#7
def encontrar_lineas_con_cadena(fichero: str, cad: str):
    try:
        lineas_encontradas = []
        with open(fichero, 'r', encoding='utf-8') as f:
            for linea in f:
                if cad.lower() in linea.lower():
                    lineas_encontradas.append(linea.strip())
        return lineas_encontradas

    except IOError as e:
        return f"Error al intentar leer el archivo: {e}"
    except Exception as i:
        return f"Error inesperado: {i}"
 
cad = "quijote"
try:
    print("################################################")
    print("TEST DE LA FUNCIÓN 7:")
    print("Las lineas donde aparecen la palabra", cad, "son:", encontrar_lineas_con_cadena("C:/Users/joaqu/git/entrega1-proyecto-Jrd545/src/resources/lin_quijote.txt", cad))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
    












#8
def encontrar_palabras_unicas(fichero: str):
    try:
        palabras_unicas = set()
        with open(fichero, 'r', encoding='utf-8') as f:
            for linea in f:
                palabras = linea.split()  # separa por espacios
                palabras_unicas.update(palabras)  # añade palabras únicas al conjunto
        return list(palabras_unicas)

    except IOError as e:
        return f"Error al intentar leer el archivo: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"
    
try:
    print("################################################")
    print("TEST DE LA FUNCIÓN 8:")
    print("Las palabras únicas en el fichero son:", encontrar_palabras_unicas("C:/Users/joaqu/git/entrega1-proyecto-Jrd545/src/resources/archivo_palabras.txt"))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")










   
#9
def longitud_promedio_lineas(file_path: str) -> Optional[float]:
    try:
        total_longitud = 0
        total_lineas = 0
        with open(file_path, 'r', encoding='utf-8') as f:
            for linea in f:
                lineas = linea.split(",")
                total_longitud += len(lineas)
                total_lineas += 1
        return total_longitud / total_lineas if total_lineas > 0 else None

    except IOError:
        return None
    except Exception:
        return None
    
try:
    print("################################################")
    print("TEST DE LA FUNCIÓN 9:")
    print("La longitud promedio de las líneas del fichero:", longitud_promedio_lineas("C:/Users/joaqu/git/entrega1-proyecto-Jrd545/src/resources/palabras_random.csv"))
    print(" ")
    print("TEST DE LA FUNCIÓN 9:")
    print("La longitud promedio de las líneas del fichero:", longitud_promedio_lineas("C:/Users/joaqu/git/entrega1-proyecto-Jrd545/src/resources/vacio.csv"))
except (TypeError, ValueError) as e:
    print(f"Error: {e}")


if __name__ == '__main__':
    pass