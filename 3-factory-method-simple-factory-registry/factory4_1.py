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
    TIPOS_DISPONIVEIS = ["pix", "cartao", "boleto"]

    tipo = input("Qual tipo de pagamento deseja usar? ")

    # Voltamos ao caos do if-else
    if tipo == "pix":
        pedido = PedidoPixFactory()
    elif tipo == "cartao":
        pedido = PedidoCartaoFactory()
    elif tipo == "boleto":
        pedido = PedidoBoletoFactory()
    else:
        raise ValueError("Tipo de pagamento inválido")

    pedido.finalizar_pedido(200)
