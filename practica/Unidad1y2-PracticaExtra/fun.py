def mas_5(lista):
    return list(filter(lambda x : len(x) > 5, lista))

def max_x(lista, x):
    return list(filter(lambda letras : len(letras) > x, lista))
