# import funciones as fun

# print(fun.sumar(2,3))

# from funciones import sumar, multi
# print(sumar(4,5))
# print(multi(4,5))

# from funciones import eliminar_duplicados

# print(eliminar_duplicados([1, 2, 2, 3, 3, 4, 5, 5, 5]))  # [1, 2, 3, 4, 5]

#from funciones import cuadrado

# lista = [4,5,6,7,8,9]
# numeros_pares = list(filter(es_par,lista))
# print(numeros_pares)

# lista = [1,2,3,4,5]

# resultado = list(map(cuadrado, lista))

# print(resultado)

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(pares)  # Output: [2, 4, 6, 8, 10]

# duplicar = list(map(lambda x: x*2, numeros))
# print(duplicar)

# mayor_5 = list(filter(lambda x: x>5, numeros))
# print(mayor_5)

#1-Ordenar una lista de números de forma ascendente:
#Escribe un programa que ordene una lista de números de forma ascendente utilizando una expresión lambda.
lista = [4,8,10,91,5,42,38,8]
print(sorted(lista))
print("-----------------------------------------------------------------")
#2-Ordenar una lista de cadenas por longitud:
#Escribe un programa que ordene una lista de cadenas por longitud, de la más corta a la más larga, utilizando una expresión lambda.
lista_cadenas = ["oro", "plata", "bronce", "cobre", "hierro"]
print(sorted(lista_cadenas, key=len))
print("-----------------------------------------------------------------")
#3-Filtrar números pares de una lista:
#Escribe un programa que filtre los números pares de una lista utilizando una expresión lambda.
pares = list(filter(lambda x : x % 2 == 0, lista))
print(pares)
print("-----------------------------------------------------------------")
#4-Filtrar palabras que comienzan con una letra específica:
#Escribe un programa que filtre las palabras de una lista que comiencen con una letra específica utilizando una expresión lambda.
palabras=["Rosario", "Buenos Aires", "Cordóba", "San Luis", "Mendoza"]
letra="M"
palabras_con_r = list(filter(lambda x: x[0] == letra, palabras))
print(palabras_con_r)
print("-----------------------------------------------------------------")
#5-Ordenar una lista de tuplas por el segundo elemento:
#Escribe un programa que ordene una lista de tuplas por el valor del segundo elemento de cada tupla utilizando una expresión lambda.
tuplas = [(9, 12), (3, 8), (6, 4), (1, 15), (7, 10)]
tuplas_ordenadas = list(sorted(tuplas, key=lambda x : x[0]))
print(tuplas_ordenadas)
print("-----------------------------------------------------------------")
#6-Filtrar números primos de una lista:
#Escribe un programa que filtre los números primos de una lista utilizando una expresión lambda y una función auxiliar para verificar si un número es primo.
from funciones import primo
lista = [4,8,10,91,5,42,38,8,9,7,15,79,37,45,1]
numeros_primos = list(filter(lambda x : primo(x), lista))
print(numeros_primos)
print("-----------------------------------------------------------------")
#7-Ordenar una lista de diccionarios por el valor de una clave específica:
#Escribe un programa que ordene una lista de diccionarios por el valor de una clave específica en cada diccionario utilizando una expresión lambda.
lista_diccionario = [
    {'nombre': 'Carlos', 'edad': 33},
    {'nombre': 'Cecilia', 'edad': 33},
    {'nombre': 'Daniel', 'edad': 43},
    {'nombre': 'Germán', 'edad': 26}
]
lista_ordenada = list(sorted(lista_diccionario, key=lambda x : x['edad']))
for x in lista_ordenada:
    print(x)
print("-----------------------------------------------------------------")
#8-Filtrar elementos que cumplen una condición específica:
#Escribe un programa que filtre los elementos de una lista que cumplan una condición específica utilizando una expresión lambda.
palabras=["Rosario", "Buenos Aires", "Cordóba", "San Luis", "Mendoza"]
letra = "o"
ultima_letra = list(filter(lambda x : x[-1] == letra, palabras))
print(ultima_letra)
print("-----------------------------------------------------------------")
#9-Ordenar una lista de cadenas ignorando mayúsculas y minúsculas:
#Escribe un programa que ordene una lista de cadenas ignorando las diferencias entre mayúsculas y minúsculas utilizando una expresión lambda.
lista = ["oro", "Plata", "bronce", "Cobre", "Hierro"]
lista_ordenada = list(sorted(lista, key=lambda x : x.lower()))
print(lista_ordenada)
print("-----------------------------------------------------------------")
#10-Filtrar elementos que contienen una subcadena específica:
#Escribe un programa que filtre los elementos de una lista que contengan una subcadena específica utilizando una expresión lambda.
lista = ["amor", "amarillo", "taza", "auto", "camion", "bicicleta", "ramo"]
subcadena = "am"
lista_subcadena = list(filter(lambda x : subcadena in x, lista))
print(lista_subcadena)
