"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from abc import ABC, abstractmethod

# Template Method: Define o esqueleto de um algoritmo em uma operação,
# deixando alguns passos para serem implementados pelas subclasses.
# Template Method permite que subclasses redefinam certos passos de um
# algoritmo sem alterar a estrutura do próprio algoritmo.


class RegraDeDesconto(ABC):
    def calcular(self, total):
        self.validar()
        self.carregar_dados()
        preco = self.calcula_preco(total)
        self.auditar()
        return preco

    def validar(self):
        print("Validando cliente...")

    def carregar_dados(self):
        print("Carregando dados...")

    def auditar(self):
        print("Auditando operação...")

    @abstractmethod
    def calcula_preco(self, total):
        pass


class DescontoVip(RegraDeDesconto):
    def calcula_preco(self, total):
        return total * 0.8


class DescontoFuncionario(RegraDeDesconto):
    def calcula_preco(self, total):
        return total * 0.7


# Uso
vip = DescontoVip()
funcionario = DescontoFuncionario()
print(vip.calcular(200))  # 160.0
print(funcionario.calcular(200))  # 140.0
