"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# Simple Factory: classe ou método responsável por criar objetos
# Factory Method: define uma interface para criar um objeto,
#                 mas deixa as subclasses decidirem qual classe instanciar.
# Problema: escolher a classe concreta a ser instanciada (dinamicamente)
# if-elses: difícil de manter e extender
# usar dict: melhora, mas ainda precisa alterar o código existente

from abc import ABC, abstractmethod


class ServicoDePedidoFactory(ABC):
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


class PedidoCartaoFactory(ServicoDePedidoFactory):
    def criar_pagamento(self):
        return PagamentoCartao()


class PedidoPixFactory(ServicoDePedidoFactory):
    def criar_pagamento(self):
        return PagamentoPix()


class PedidoBoletoFactory(ServicoDePedidoFactory):
    def criar_pagamento(self):
        return PagamentoBoleto()


class Registry:
    def __init__(self):
        self._mapa = {}

    def registrar(self, chave, classe):
        self._mapa[chave] = classe

    def criar(self, chave) -> ServicoDePedidoFactory:
        classe = self._mapa.get(chave)
        if not classe:
            raise ValueError("Tipo inválido")
        return classe()

    # Observe que Registry não é Singleton.


if __name__ == "__main__":
    registro = Registry()
    registro.registrar("pix", PedidoPixFactory)
    registro.registrar("cartao", PedidoCartaoFactory)
    registro.registrar("boleto", PedidoBoletoFactory)

    tipo = input("Tipo de pagamento: ")
    pedido = registro.criar(tipo)
    pedido.finalizar_pedido(100)
