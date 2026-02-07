"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from functools import wraps


def singleton(cls):
    """Decorator que transforma uma classe em singleton."""
    instancia = None

    @wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal instancia  # Permite modificar a variável 'instancia' do escopo externo
        if instancia is None:
            instancia = cls(*args, **kwargs)
        return instancia

    return wrapper


@singleton
class Configuracao:
    def __init__(self):
        print("Carregando configurações...")
        self.valor = 42


config1 = Configuracao()
config2 = Configuracao()
config3 = Configuracao()

print(config1 is config2 is config3)  # True

# equivalente a
# Configuracao = singleton(Configuracao)
# config1 = Configuracao()
# ou: config1 = singleton(Configuracao)()
