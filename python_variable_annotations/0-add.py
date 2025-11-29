#!/usr/bin/env python3
"""
Mathematical Utilities Module.

Este módulo proporciona funciones simples para operaciones matemáticas
básicas. Incluye la función 'floor' para obtener el suelo de un número.
"""

import math


def floor(n: float) -> int:
    """
    Devuelve el valor floor de un número flotante.

    Toma un número de tipo float y retorna su parte entera inferior,
    utilizando la función 'floor' del módulo estándar 'math'.

    :param n: Número flotante del cual se quiere obtener el floor.
    :return: El floor del número 'n' como un entero.

    Ejemplos:
    >>> floor(3.14)
    3
    >>> floor(-2.7)
    -3
    >>> floor(5.0)
    5
    """
    return math.floor(n)
