"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

# E quando o tipo de objeto não é conhecido até a hora da execução?
# meios de pagamento: tipo (pix, cartao, boleto) vem de um arquivo JSON

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

# Dicionário precisa ser atualizado manualmente
# Solução ainda é centralizada
