"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# Mais um tipo de cliente
# Black friday
# parceria X
# parceria Y

from dataclasses import dataclass


@dataclass
class Cliente:
    nome: str
    tipo: str
    parceiro: str = None


def calcular_preco(cliente, total):
    if cliente.tipo == "vip":
        preco = total * 0.8
    elif cliente.tipo == "novo":
        preco = total * 0.9
    elif cliente.tipo == "funcionario":
        preco = total * 0.7
    elif cliente.tipo == "parceria":
        preco = total * 0.85
        if cliente.parceiro == "empresa_x":
            preco -= 10
        elif cliente.parceiro == "empresa_y":
            preco -= 5
    elif cliente.tipo == "black_friday":
        preco = total * 0.5
        if total > 500:
            preco *= 0.9
    else:
        preco = total

    return preco


# Code smells
# - complexidade crescente (muitos ifs)
# - difícil manutenção (adicionar novos tipos de clientes)
# - difícil testabilidade (testar todas as combinações)
# - violação do princípio aberto/fechado (modificar a função para adicionar novos tipos
#   de clientes)
# - baixa coesão (a função faz muitas coisas diferentes)
# - alta acoplamento (a função depende de muitos detalhes dos clientes)
# - difícil reutilização (não é possível reutilizar a lógica de cálculo de preço
#  em outros contextos)


# Solução: Separar as estratégias de cálculo de preço em objetos diferentes
