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


class PedidoCartaoFactory(ServicoDePedido):
    def criar_pagamento(self):
        return PagamentoCartao()


class PedidoPixFactory(ServicoDePedido):
    def criar_pagamento(self):
        return PagamentoPix()


class PedidoBoletoFactory(ServicoDePedido):
    def criar_pagamento(self):
        return PagamentoBoleto()


if __name__ == "__main__":
    MAPA_PEDIDOS = {
        "pix": PedidoPixFactory,
        "cartao": PedidoCartaoFactory,
        "boleto": PedidoBoletoFactory,
    }

    tipo = input("Tipo de pagamento: ")
    classe_pedido = MAPA_PEDIDOS.get(tipo)

    if not classe_pedido:
        raise ValueError("Tipo inválido")

    pedido = classe_pedido()
    pedido.finalizar_pedido(100)
