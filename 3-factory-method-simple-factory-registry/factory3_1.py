"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

from abc import ABC, abstractmethod

# E se for preciso adicionar novos tipos sem alterar o código existente?

# A Simple Factory centraliza a criação
# Mas toda vez que adicionamos um tipo novo, mexemos na fábrica existente
# Factory Method: Define uma interface para criar um objeto,
#                 mas deixa as subclasses decidirem qual classe instanciar.


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


class PedidoCartaoFactory(ServicoDePedidoFactory):
    def criar_pagamento(self):
        return PagamentoCartao()


class PedidoPixFactory(ServicoDePedidoFactory):
    def criar_pagamento(self):
        return PagamentoPix()


if __name__ == "__main__":
    pedido1 = PedidoPixFactory()
    pedido1.finalizar_pedido(250)

    pedido2 = PedidoCartaoFactory()
    pedido2.finalizar_pedido(180)


# Benefícios
# - Extensibilidade
# - baixo acoplamento
# - adere ao princípio Open/Closed

# Limitações
# - aumenta o número de classes
# - camada extra de abstração
