"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# ruff: noqa: E402
# preservando metadados


def adicionar_log(func):
    def wrapper(a, b):
        resultado = func(a, b)
        print(f"Executando {func.__name__}({a}, {b}) = {resultado}")
        return resultado

    return wrapper


@adicionar_log
def somar(a, b):
    return a + b


print(somar.__name__)  # saída: wrapper

import functools


def adicionar_log(func):
    @functools.wraps(func)
    def wrapper(a, b):
        resultado = func(a, b)
        print(f"Executando {func.__name__}({a}, {b}) = {resultado}")
        return resultado

    return wrapper


@adicionar_log
def somar(a, b):
    return a + b


print(somar.__name__)  # saída: somar
