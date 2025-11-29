#!/usr/bin/env python3
"""
String Utilities Module.

Este módulo proporciona funciones simples para operaciones básicas con cadenas.
Actualmente, contiene la función 'concat' para concatenar dos cadenas.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatena dos cadenas de texto.

    Toma dos strings y devuelve una nueva cadena que es la unión de ambas,
    en el mismo orden en que se pasan como argumentos.

    :param str1: La primera cadena.
    :param str2: La segunda cadena.
    :return: La concatenación de 'str1' y 'str2'.

    Ejemplos:
    >>> concat("Hola, ", "mundo")
    'Hola, mundo'
    >>> concat("foo", "bar")
    'foobar'
    >>> concat("", "test")
    'test'
    """
    return str1 + str2
