"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from abc import ABC, abstractmethod


class RegraDeDesconto(ABC):
    @abstractmethod
    def calcular(self, total):
        pass


class DescontoVip(RegraDeDesconto):
    def calcular(self, total):
        return total * 0.8


class DescontoNovo(RegraDeDesconto):
    def calcular(self, total):
        return total * 0.9


class DescontoFuncionario(RegraDeDesconto):
    def calcular(self, total):
        return total * 0.7


class SemDesconto(RegraDeDesconto):
    def calcular(self, total):
        return total


class Cliente:
    def __init__(self, nome, estrategia: RegraDeDesconto):
        self.nome = nome
        self.regra_de_desconto = estrategia


def calcular_preco(cliente: Cliente, total):
    # polimorfismo em ação
    return cliente.regra_de_desconto.calcular(total)


maria = Cliente("Maria", DescontoVip())
joao = Cliente("João", DescontoNovo())
ana = Cliente("Ana", SemDesconto())

print(calcular_preco(maria, 200))  # 160
print(calcular_preco(joao, 200))  # 180
print(calcular_preco(ana, 200))  # 200

# Padrão Strategy:
# Definição: Define uma família de algoritmos, encapsula cada um deles
# e os torna intercambiáveis. Strategy permite que o algoritmo varie
# independentemente dos clientes que o utilizam.

# Vantagens:
# - Extensibilidade: novas estratégias podem ser adicionadas sem modificar o código existente.
# - Manutenção: cada estratégia é isolada, facilitando a manutenção e testes.
# - Coesão: cada classe tem uma única responsabilidade.
# - Aderência ao princípio aberto/fechado: o código está aberto para extensão,
#   mas fechado para modificação.
# - Reutilização: estratégias podem ser reutilizadas em diferentes contextos.
# - Baixo acoplamento: o cliente depende apenas da interface abstrata, não das implementações concretas.
# - Testabilidade: cada estratégia pode ser testada isoladamente.
# - Clareza: o código fica mais claro e fácil de entender (sem muitos ifs).
