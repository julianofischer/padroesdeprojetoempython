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
        print("Validando cliente...")  # repetido
        print("Carregando dados...")  # repetido
        preco = total * 0.8  # parte variável
        print("Auditando operação...")  # repetido
        return preco


class DescontoFuncionario(RegraDeDesconto):
    def calcular(self, total):
        print("Validando cliente...")
        print("Carregando dados...")
        preco = total * 0.7  # parte variável
        print("Auditando operação...")
        return preco
