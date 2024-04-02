"""Tuple, Enumerate, Zip, Args.


Contexto: Se tiene un programa que lee diferentes listas de una tabla en una
base de datos y se quieren combinar estas listas para que luego puedan crearse
los objetos de la capa de negocio.
"""


from typing import Any, List, Tuple

nombre_articulos = ["ventana", "lámpara", "shampoo"]
precio_articulos = [100.48, 16.42, 5.20]


def combinar_basico(nombres: List[str], precios: List[float]) -> Tuple[Any]:
    """Toma dos listas y devuelve una tupla de duplas con los componentes de
    las listas.

    Restricción:
        - Utilizar un bucle FOR.
        - Utilizar la función range.
        - Utilizar índices.
    """
    lista = []
    for x in range(len(nombres)):
        lista.append((nombres[x], precios[x]))
    return tuple(lista)

# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48),
    ("lámpara", 16.42),
    ("shampoo", 5.2),
)

assert combinar_basico(nombre_articulos, precio_articulos) == respuesta
# NO MODIFICAR - FIN


###############################################################################


id_articulos = [6852, 1459, 3578]


def combinar_enumerate(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:  # noqa: E501
    """Re-Escribir utilizando enumerate y agregando un nuevo componente.

    Restricción:
        - Utilizar un bucle FOR.
        - No Utilizar la función range.
        - No Utilizar la función zip.

    Referencia: https://docs.python.org/3/library/functions.html#enumerate
    """
    lista = []
    for x, id in enumerate(ids):
        lista.append((nombres[x], precios[x], id))

    return tuple(lista)

# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar_enumerate(nombre_articulos, precio_articulos, id_articulos) == respuesta  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


id_articulos = [6852, 1459, 3578]


def combinar_zip(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:  # noqa: E501
    """Re-Escribir utilizando zip.

    Restricción:
        - Utilizar un bucle FOR.
        - No utilizar la función range.
        - No utilizar la función enumerate.
        - No utilizar índices.
    Referencia: https://docs.python.org/3/library/functions.html#zip
    """
    lista = []
    for x, y, id in zip(nombres, precios, ids):
        lista.append((x, y, id))
    return tuple(lista)

# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

assert combinar_zip(nombre_articulos, precio_articulos, id_articulos) == respuesta  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################


id_articulos = [6852, 1459, 3578]


def combinar_zip(nombres: List[str], precios: List[float], ids: List[int]) -> Tuple[Any]:  # noqa: E501
    """Re-Escribir utilizando zip.

    Restricción:
        - Utilizar un bucle FOR.
        - No utilizar la función range.
        - No utilizar la función enumerate.
        - No utilizar índices.
    Referencia: https://docs.python.org/3/library/functions.html#zip
    """
    

# NO MODIFICAR - INICIO
respuesta = (
    ("ventana", 100.48, 6852),
    ("lámpara", 16.42, 1459),
    ("shampoo", 5.2, 3578),
)

#assert combinar_zip(nombre_articulos, precio_articulos, id_articulos) == respuesta
# NO MODIFICAR - FIN
