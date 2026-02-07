"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from abc import ABC, abstractmethod


# Registry de classes para o Factory Method
class Registry:
    _map = {}

    @classmethod
    def register(cls, key, classe):
        cls._map[key] = classe

    @classmethod
    def create(cls, key):
        classe = cls._map.get(key)
        if not classe:
            raise ValueError("Tipo inválido")
        return classe()


def registrar_factory(nome):
    def decorator(classe):
        Registry.register(nome, classe)
        return classe

    return decorator


class ServicoDePedido(ABC):
    @abstractmethod
    def criar_pagamento(self):
        """Factory Method — cria o tipo de pagamento adequado."""
        pass

    def finalizar_pedido(self, total):
        pagamento = self.criar_pagamento()  # usa o método fábrica
        pagamento.processar(total)


class PagamentoCartao:
    def processar(self, valor):
        print(f"💳 Pagamento no cartão de R$ {valor} processado.")


class PagamentoPix:
    def processar(self, valor):
        print(f"⚡ Pagamento via PIX de R$ {valor} processado.")


class PagamentoBoleto:
    def processar(self, valor):
        print(f"⚡ Pagamento via Boleto de R$ {valor} processado.")


@registrar_factory("cartao")
class PedidoCartao(ServicoDePedido):
    def criar_pagamento(self):
        return PagamentoCartao()


@registrar_factory("pix")
class PedidoPix(ServicoDePedido):
    def criar_pagamento(self):
        return PagamentoPix()


@registrar_factory("boleto")
class PedidoBoleto(ServicoDePedido):
    def criar_pagamento(self):
        return PagamentoBoleto()


# @registrar_factory é açúcar sintático para:
registrar_factory("boleto")(PedidoBoleto)

if __name__ == "__main__":
    tipo = input("Tipo de pagamento: ")
    pedido = Registry.create(tipo)
    pedido.finalizar_pedido(100)
