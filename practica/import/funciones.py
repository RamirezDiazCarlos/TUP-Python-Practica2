def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multi(a,b):
    return a*b

def dividir(a,b):
    return a/b

def eliminar_duplicados(lista):
    nueva_lista = []
    for x in lista:
        if x not in nueva_lista:
            nueva_lista.append(x)
    return nueva_lista

def es_par(lista):
    return lista % 2 == 0

def cuadrado(lista):
    return lista**2



