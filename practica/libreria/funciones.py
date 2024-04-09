def cortar_decimales(num:float) -> int:
    return int(num)

def elevar(x:int, y:int = 2) -> int:
    resultado = 1
    for i in range(0,y):
        resultado = resultado * x
    return resultado # or "Fallo el calculo" (para mostrar en caso de que falle)

def agregar_elementos(lista:list, *elementos):
    nueva_lista = lista[:] # copiar en una nueva posición de memoria es necesario los : dentro de los corchetes
    for x in elementos:
        nueva_lista.append(x)
    return nueva_lista