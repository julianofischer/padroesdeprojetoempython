"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    tipo: str


def calcular_preco(cliente, total):
    if cliente.tipo == "vip":
        return total * 0.8
    elif cliente.tipo == "novo":
        return total * 0.9
    elif cliente.tipo == "funcionario":
        return total * 0.7
    else:
        return total
