"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# ruff: noqa: E731

# Em Python, funções são “cidadãos de primeira classe”:
# - podem ser passadas como argumentos
# - guardadas em variáveis
# - retornadas por outras funções
# - armazenadas em listas/dicionários
# - substituídas em runtime


def desconto_vip(total):
    return total * 0.8


def desconto_novo(total):
    return total * 0.9


def desconto_funcionario(total):
    return total * 0.7


def sem_desconto(total):
    return total


def calcular_preco(total, estrategia):
    return estrategia(total)


# Lambdas: funções anônimas, definidas em uma única linha
soma = lambda a, b: a + b

desconto_estudante = lambda total: total * 0.85
black_friday = lambda total: total * 0.5 if total <= 500 else total * 0.5 * 0.9
parceria_empresa_x = lambda total: total * 0.85 - 10
parceria_empresa_y = lambda total: total * 0.85 - 5

# Uso
print(calcular_preco(200, desconto_vip))  # 160.0
print(calcular_preco(200, desconto_novo))  # 180.0
print(calcular_preco(200, desconto_funcionario))  # 140.0
print(calcular_preco(200, sem_desconto))  # 200.0
print(calcular_preco(200, desconto_estudante))  # 170.0
print(calcular_preco(600, black_friday))  # 270.0
print(calcular_preco(200, parceria_empresa_x))  # 160.0
print(calcular_preco(200, parceria_empresa_y))  # 165.0

# Não é necessário atribuir a uma variável
print(calcular_preco(300, lambda total: total * 0.75))
