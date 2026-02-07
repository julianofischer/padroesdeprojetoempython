"""
Autor: Juliano Fischer Naves
https://github.com/julianofischer/
"""

class ServicoDePagamento:
    def processar(self, valor):
        print(f"💳 Pagamento de R$ {valor} processado.")


class ServicoDePix:
    def processar(self, valor):
        print(f"⚡ Pagamento via PIX de R$ {valor} processado.")


class ServicoDePedido:
    def __init__(self, tipo_pagamento="cartao"):
        if tipo_pagamento == "cartao":
            self.pagamento = ServicoDePagamento()
        elif tipo_pagamento == "pix":
            self.pagamento = ServicoDePix()
        else:
            raise ValueError("Tipo de pagamento inválido")

    def finalizar_pedido(self, total):
        self.pagamento.processar(total)


# Teste
pedido = ServicoDePedido("cartao")
pedido.finalizar_pedido(120)

# mais flexível
# porém, ServicoDePedido sabe demais sobre as classes concretas
# estamos adiando o problema
# lembrar “Quem cria a dependência não é quem a usa.”
