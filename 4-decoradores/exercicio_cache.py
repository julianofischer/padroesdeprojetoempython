"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

import time


def cache(func):
    """
    Decorator para implementar cache manual.
    Funciona apenas para funções com 1 argumento.
    """
    cache_dict = {}

    def wrapper(x):
        # verifica se já está no cache
        if x in cache_dict:
            print(f"[CACHE] Usando valor armazenado para {x}")
            return cache_dict[x]

        # calcula normalmente e armazena
        print(f"[CALCULO] Calculando valor para {x}...")
        resultado = func(x)
        cache_dict[x] = resultado

        return resultado

    return wrapper


# ============ Testes ============


@cache
def calcula_pesado(n):
    print("Função original executando...")
    time.sleep(1)  # simula operação lenta
    return n * n


if __name__ == "__main__":
    print(calcula_pesado(5))  # cálculo real
    print(calcula_pesado(5))  # valor vindo do cache
    print(calcula_pesado(10))  # novo cálculo
    print(calcula_pesado(10))  # cache
