# 1. Escribe un programa que pida al usuario ingresar su edad y luego imprima un mensaje
# indicando si es mayor de edad o no.
"""edad = int(input("Ingrese su edad:"))
if edad > 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")"""
# 2. Escribe un programa que tome una lista de números y calcule la suma de todos los
# elementos.
"""lista = [1,2,3,4,5,6]
print(sum(lista))"""
# 3. Escribe un programa que imprima los números del 1 al 10 utilizando un bucle while.
"""x = 1
while x <= 10:
    print(x)
    x += 1"""
# 4. Escribe un programa que tome una lista de números y devuelva solo los números pares.
"""lista = [1,2,3,4,5,6,7,8,9,10]
pares = [x for x in lista if x % 2 == 0]
print(pares)"""
# 5. Escribe un programa que tome dos tuplas e imprima un diccionario donde las primeras
# tuplas sean las claves y las segundas tuplas sean los valores correspondientes.
"""tupla1 = ("Uno", "Dos", "Tres")
tupla2 = (1,2,3)
diccionario = {}
for x in range(0, len(tupla1)):
    diccionario[tupla1[x]] = tupla2[x]
print(diccionario)"""
# 6. Escribe un programa que itere sobre un diccionario e imprima solo las claves que sean
# strings.
"""diccionario = {
    "nombre": "Carlos",
    2: "Ramirez Diaz",
    "ciudad": "Rosario",
    4: "33"
}
for x in diccionario.keys():
    if type(x) == str:
        print(x)"""
# 7. Escribe una función llamada es_primo que tome un número como argumento y
# devuelva True si es primo y False si no lo es.
"""def es_primo(num):
    if num <=1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

print(es_primo(10))
print(es_primo(7))"""
# 8. Escribe una función llamada contador_letras que tome una cadena como argumento y
# devuelva un diccionario donde las claves sean las letras de la cadena y los valores sean
# la cantidad de veces que aparece cada letra.

# 9. Escribe una función llamada eliminar_duplicados que tome una lista como argumento y
# devuelva una nueva lista con los elementos únicos de la lista original, manteniendo el
# orden.
"""def eliminar_duplicado(lista):
    unicos = []
    for x in lista:
        if x not in unicos:
            unicos.append(x)
    return unicos

lista = [1,1,2,2,3,3,4,4,5,5]
print(eliminar_duplicado(lista))"""
# 10. Escribe un programa que pida al usuario ingresar una lista de números y luego imprima
# el mayor de ellos utilizando una función llamada encontrar_mayor.
"""def encontrar_mayor(lista):
    mayor = 0
    for x in lista:
        if x > mayor:
            mayor = x
    return mayor

lista = []
for x in range(5):
    z = int(input("ingrese un número: "))
    lista.append(z)

print(encontrar_mayor(lista))"""
# 11. Escribe una función para contar vocales en una cadena
"""def vocales(cadena):
    vocales = "aeiou"
    contador = 0
    for x in cadena:
        if x in vocales:
            contador += 1
    return contador

cadena = "como estas"
print(vocales(cadena))"""
# 12. Escribe una función que devuelve una copia de una lista en orden invertido.
"""def lista_invertida(lista):
    return lista[::-1]

lista = [1,2,3,4,5]
print(lista_invertida(lista))"""
# 13. Escribe un programa que ordene una lista de números de forma ascendente utilizando
# una expresión lambda.
"""lista = [4,2,5,7,3,6,1]
lista_ordenada = sorted(lista)
print(lista_ordenada)"""
# 14. Escribe un programa que ordene una lista de cadenas por longitud, de la más corta a la
# más larga, utilizando una expresión lambda.
"""lista = ["oro", "cobre", "hierro", "plata", "aluminio"]
lista_ordenada = sorted(lista, key = lambda x : len(x))
print(lista_ordenada)"""
# 15. Escribe un programa que filtre los números pares de una lista utilizando una expresión
# lambda.
"""lista = [1,2,3,4,5,6,7,8,9,10,11]
pares = list(filter(lambda x : x % 2 == 0, lista))
print(pares)"""
# 16. Escribe un programa que filtre los números impares de una lista utilizando una
# expresión lambda.
"""lista = [1,2,3,4,5,6,7,8,9,10,11]
pares = list(filter(lambda x : x % 2 != 0, lista))
print(pares)"""
# 17. Escribe una función que filtre las palabras de una lista que comiencen con una letra
# específica utilizando una expresión lambda.
"""palabras=["Rosario", "Buenos Aires", "Cordóba", "San Luis", "Mendoza"]
letra="M"
palabras_con_x = list(filter(lambda x: x[0] == letra, palabras))
print(palabras_con_x)"""
# 18. Escribe un programa que ordene una lista de tuplas por el valor del segundo elemento
# de cada tupla utilizando una expresión lambda.
"""lista_tuplas = [(4,5), (21,3), (54,2), (74,4), (23,1)]
tuplas_ordenadas = sorted(lista_tuplas, key=lambda x : x[1])
print(tuplas_ordenadas)"""
# 19. Escribe un programa que filtre los números primos de una lista utilizando una expresión
# lambda y una función auxiliar para verificar si un número es primo.
"""def primo(num):
    if num <= 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

lista = [4,8,10,91,5,42,38,8,9,7,15,79,37,45,1]
numeros_primos = list(filter(lambda x : primo(x), lista))
print(numeros_primos)"""
# 20. Escribe un programa que ordene una lista de diccionarios por el valor de una clave
# específica en cada diccionario utilizando una expresión lambda.
"""lista_diccionario = [
    {'nombre': 'Carlos', 'edad': 33},
    {'nombre': 'Cecilia', 'edad': 33},
    {'nombre': 'Daniel', 'edad': 43},
    {'nombre': 'Germán', 'edad': 26}
]

lista_ordenada = sorted(lista_diccionario, key=lambda x : x['edad'])
for x in lista_ordenada:
    print(x)"""
# 21. Escribe una función que filtre los elementos de una lista numérica qué no sean primos
# utilizando una expresión lambda.
"""def primo(num):
    if num <= 1:
        return True
    for x in range(2, num):
        if num % x == 0:
            return True
    return False

lista = [4,8,10,91,5,42,38,8,9,7,15,79,37,45,1]
numeros_primos = list(filter(lambda x : primo(x), lista))
print(numeros_primos)"""
# 22. En un módulo separado, escribe una función que filtre los elementos de una lista de
# string qué su longitud sea mayor a 5 utilizando una expresión lambda.
"""from fun import mas_5
palabras = ["elefante", "gato", "perro", "computadora", "montaña"]
print(mas_5(palabras))"""
# 23. En un módulo separado, escribe una función que filtre los elementos de una lista de
# string qué su longitud sea mayor a x (pasado cómo parámetro) utilizando una expresión
# lambda.
from fun import max_x
palabras = ["elefante", "gato", "perro", "computadora", "montaña"]
letras = 7
print(max_x(palabras, letras))
# 24. En un módulo separado, escribe una función que ordene una lista de cadenas ignorando
# las diferencias entre mayúsculas y minúsculas utilizando una expresión lambda.

# 25. En un módulo separado, escribe una función que filtre los elementos de una lista que
# contengan una subcadena específica utilizando una expresión lambda.

# 26. En un módulo separado, crear una función lambda para generar números cuadrados.

# 27. En un módulo separado, crear una función lambda que cuente la cantidad de números
# pares de una lista.

# 28. En un módulo separado, crear una función lambda que cuente la cantidad de números
# impares de una lista.
