# import funciones as fun
# print(fun.sumar(2,3))

# from funciones import sumar, multi
# print(sumar(4,5))
# print(multi(4,5))

# from funciones import eliminar_duplicados

# print(eliminar_duplicados([1, 2, 2, 3, 3, 4, 5, 5, 5]))  # [1, 2, 3, 4, 5]

from funciones import cuadrado

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

lista = [4,8,10,91,5,42,38,8]
print(sorted(lista))

lista_cadenas = ["oro", "plata", "bronce", "cobre", "hierro"]
print(sorted(lista_cadenas, key=len))

pares = list(filter(lambda x: x % 2 == 0, lista))
print(pares)

palabras=["Rosario", "Buenos Aires", "Cordóba", "San Luis", "Mendoza"]
letra="M"
palabras_con_r = list(filter(lambda x: x[0] == letra, palabras))
print(palabras_con_r)

tuplas = [(9, 12), (3, 8), (6, 4), (1, 15), (7, 10)]
tuplas_ordenadas = list(sorted(tuplas, key=lambda x:x[0]))
print(tuplas_ordenadas)

