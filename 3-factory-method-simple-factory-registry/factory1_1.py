"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

class ServicoDePagamento:
    def processar(self, valor):
        print(f"💳 Pagamento de R$ {valor} processado.")


class ServicoDePedido:
    def __init__(self):
        self.pagamento = ServicoDePagamento()  # <- criação rígida
        # - alto acoplamento
        # - baixa flexibilidade

    def finalizar_pedido(self, total):
        self.pagamento.processar(total)


# Problema: alta dependência entre classes devido à criação rígida de objetos.
